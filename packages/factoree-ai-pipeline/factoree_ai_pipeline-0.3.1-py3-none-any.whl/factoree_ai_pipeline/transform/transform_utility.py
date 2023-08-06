from abc import ABC, abstractmethod
from typing import Generic, final
from logging import Logger
from typing import TypeVar
from factoree_ai_pipeline.file.file_types import S3JsonFile
from factoree_ai_pipeline.sensor_type import SensorType
from factoree_ai_pipeline.system_params import SUB_COMPONENT_BRONZE, SUB_COMPONENT_SILVER

DATA_TYPE = TypeVar('DATA_TYPE')
TransformOutput = list[S3JsonFile]
TransformTuple = (TransformOutput, DATA_TYPE)


class TransformUtility(ABC, Generic[DATA_TYPE]):
    def __init__(
            self,
            logger: Logger,
            is_test: bool = False
    ):
        self.logger = logger
        self.is_test = is_test

    @final
    def transform(self, bucket_name: str, file_data: DATA_TYPE, timezone_name: str) -> TransformTuple:
        transformed_data, filename_by_sensor_type, errors = self.transform_data_to_silver_format(
            file_data, timezone_name
        )
        output_files: list[S3JsonFile] = TransformUtility.construct_output_files(
            bucket_name, transformed_data, filename_by_sensor_type
        )
        return output_files, errors

    @abstractmethod
    def transform_data_to_silver_format(
            self, file_data: DATA_TYPE, timezone_name: str
    ) -> (dict[SensorType, dict], dict[SensorType, str], list[DATA_TYPE]):
        pass

    @staticmethod
    def construct_output_files(
            bucket_name: str,
            data_by_sensor_type: dict[SensorType, dict],
            filename_by_sensor_type: dict[SensorType, str]
    ) -> list[S3JsonFile]:
        return [S3JsonFile(
            bucket_name.replace(SUB_COMPONENT_BRONZE, SUB_COMPONENT_SILVER),
            filename_by_sensor_type[sensor_type],
            data_by_sensor_type[sensor_type])
            for sensor_type in data_by_sensor_type]
