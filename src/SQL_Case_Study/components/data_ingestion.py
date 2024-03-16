import pandas as pd
import os,sys
from src.SQL_Case_Study.logger import logging
from src.SQL_Case_Study.exception import CustomException
from dataclasses import dataclass
from src.SQL_Case_Study.utils import get_data

@dataclass
class DataIngestionConfig:
    raw_data_path=os.path.join("data",'raw.csv')

class DataIngestion:
    def __init__(self):
        self.data_ingestion=DataIngestionConfig()
    
    def initisate_data_ingestion(self):
        logging.info("Reading the data from souce")
        try:
            data=get_data()[0]
            
            logging.info("Making Directory")
            os.makedirs(os.path.dirname(self.data_ingestion.raw_data_path),exist_ok=True)

            logging.info("Saving the data")
            data.to_csv(self.data_ingestion.raw_data_path,index=False,header=True)

            return self.data_ingestion.raw_data_path
        except Exception as e:
            raise CustomException(e,sys)
