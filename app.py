from src.SQL_Case_Study.logger import logging
from src.SQL_Case_Study.exception import CustomException
import sys
from src.SQL_Case_Study.utils import get_data
from src.SQL_Case_Study.components.data_ingestion import DataIngestion
from src.SQL_Case_Study.components.data_ingestion import DataIngestionConfig


if __name__=="__main__":
    logging.info("excution start...")
    try:
        data=DataIngestion()
        data.initisate_data_ingestion()
    except Exception as e:
        raise CustomException(e,sys)