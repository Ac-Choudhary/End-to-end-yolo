import sys,os
from Detection.logger import logging
from Detection.exception import AppException
from Detection.components.data_ingestion import DataIngestion
from Detection.entity.config_entity import (DataIngestionConfig)
from Detection.entity.artifacts_entity import (DataIngestionArtifact)

class TrainPipelines:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def start_data_ingestion(self)->DataIngestionArtifact:
        try:
            logging.info(
                "Entered the start_data_ingestion method of TrainPipeline class"
            )
            logging.info("Getting the data from url")

            data_ingestion =DataIngestion(
                data_ingestion_config=self.data_ingestion_config
            )

            data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
            logging.info("Got the data from URL")
            logging.info(
                "Exited the start_data_ingestion method of TrainPipeline class"
            )
            return data_ingestion_artifact

        except Exception as e:
            raise AppException(e, sys)
        
    def run_pipeline(self)->None:
        try: data_ingestion_artifact=self.start_data_ingestion()
        except Exception as e:
            raise AppException(e, sys)