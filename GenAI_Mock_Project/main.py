from src.logging import logger
from src.exception.exception import ProjectException
from src.components.data_ingestation import DataIngestion
from src.components.data_ingestation import DataIngestionArifact
from src.components.data_ingestation import DataIngestionConfig
import sys


if __name__=='__main__':
    data_ingestion = DataIngestion()
    train_data, test_data = data_ingestion.initiate_data_ingestion()