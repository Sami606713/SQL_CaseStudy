from src.SQL_Case_Study.logger import logging
from src.SQL_Case_Study.exception import CustomException
import sys
from src.SQL_Case_Study.utils import get_data

if __name__=="__main__":
    logging.info("excution start...")
    try:
        get_data()
    except Exception as e:
        raise CustomException(e,sys)