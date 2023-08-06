from datetime import datetime
from logging import Logger
from factoree_ai_pipeline.file.file_utils import get_silver_file_name
from factoree_ai_pipeline.sensor_type import SensorType, parse_sensor_type
from factoree_ai_pipeline.transform.transform_utility import TransformUtility

Csv = list[list[int | float | str | datetime]]
TIME_KEY = 'time'
VALUES_KEY_NAME = 'values'
PHASE_ID_KEY = 'phase_id'
DATA_KEY = 'data'
DATA_TYPE_KEY = 'data_type'


class CsvTransformUtility(TransformUtility[Csv]):
    def __init__(
            self,
            timestamp_column: int,
            logger: Logger,
            is_test: bool = False
    ):
        super(CsvTransformUtility, self).__init__(logger, is_test)
        self.timestamp_column = timestamp_column

    def transform_data_to_silver_format(
            self, file_data: Csv, timezone_name: str
    ) -> (dict[SensorType, dict], dict[SensorType, str], Csv):
        columns_by_sensor_type, errors = self.group_columns_by_sensor_type(file_data)
        transformed_data_by_sensor_type, filenames = self.transform_grouped_data_to_silver_format(
            columns_by_sensor_type,
            file_data
        )
        return transformed_data_by_sensor_type, filenames, errors

    def transform_grouped_data_to_silver_format(
            self, columns_by_sensor_type: dict[SensorType, list[int]], file_data: Csv
    ) -> (dict[SensorType, dict], dict[SensorType, str]):
        transformed_data_by_sensor_type: dict[SensorType, dict] = {}
        filenames: dict[SensorType, str] = {}

        for sensor_type in columns_by_sensor_type.keys():
            if sensor_type not in filenames.keys():
                filenames[sensor_type] = self.get_silver_filename_for_sensor_type_samples(
                    sensor_type,
                    file_data,
                    columns_by_sensor_type.get(sensor_type)[0]
                )

            data_of_sensor_type = transformed_data_by_sensor_type.get(sensor_type, {DATA_KEY: []})
            for row in range(1, len(file_data)):
                if sensor_type == SensorType.STEP:
                    key = PHASE_ID_KEY
                    value = file_data[row][columns_by_sensor_type.get(sensor_type)[0]]
                else:
                    value = {}
                    for column in columns_by_sensor_type.get(sensor_type):
                        value[file_data[0][column]] = file_data[row][column]
                    key = VALUES_KEY_NAME

                data_of_sensor_type.get(DATA_KEY).append({
                    TIME_KEY: file_data[row][self.timestamp_column],
                    key: value
                })
            transformed_data_by_sensor_type[sensor_type] = data_of_sensor_type

        return transformed_data_by_sensor_type, filenames

    def group_columns_by_sensor_type(self, file_data: Csv) -> dict[SensorType, list[int]]:
        result: dict[SensorType, list[int]] = {}

        for i in range(1, len(file_data[0])):
            parsed_type: SensorType = self.extract_sensor_type(file_data[0][i])
            columns_of_type = result.get(parsed_type, [])
            columns_of_type.append(i)
            result[parsed_type] = columns_of_type

        return result

    # noinspection PyMethodMayBeStatic
    def extract_sensor_type(self, tag: str) -> SensorType:
        tag_parts = tag.split('-')
        return parse_sensor_type(tag_parts[1]) or parse_sensor_type(tag_parts[2])

    def get_silver_filename_for_sensor_type_samples(
            self,
            sensor_type: SensorType,
            file_data: Csv,
            column: int
    ) -> str:
        tag = file_data[0][column]
        first_sample = file_data[1][self.timestamp_column]
        last_sample = file_data[-1][self.timestamp_column]
        facility = tag.split('-')[0]

        if sensor_type == SensorType.STEP:
            result = get_silver_file_name(
                sensor_type.value.get(DATA_TYPE_KEY),
                facility,
                sensor_type.name,
                first_sample,
                last_sample,
                self.is_test,
                tag.split('-')[1]
            )
        else:
            result = get_silver_file_name(
                sensor_type.value.get(DATA_TYPE_KEY),
                facility,
                sensor_type.name,
                first_sample,
                last_sample,
                self.is_test
            )
        return result
