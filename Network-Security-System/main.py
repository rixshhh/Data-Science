import sys
from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig

if __name__ == "__main__":
    try:
        training_pipelin_config = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(training_pipelin_config)
        data_ingestion = DataIngestion(data_ingestion_config)
        logging.info('Initiate the data ingestion.')
        dataIngestionArtifact = data_ingestion.initiate_data_ingestion()

        print(dataIngestionArtifact)
        
    except Exception as e:
        raise NetworkSecurityException(e, sys)