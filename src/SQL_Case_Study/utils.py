import pandas as pd
import os,sys
from src.SQL_Case_Study.logger import logging
from src.SQL_Case_Study.exception import CustomException
import pymysql
from dotenv import load_dotenv

logging.info("loadin the environment variable")
load_dotenv()
host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv("db")

def get_data():
    try:
        logging.info("setting the database connecction")
        conn=pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=db
        )
        logging.info("datanase connection successfull")
        logging.info("Reading the data")
        
        data=pd.read_sql_query("select * from exams",con=conn)
        print(data.head())
        
        return [data,conn]
        
    except Exception as e:
        logging.info('error for connecting the database')
        raise CustomException(e,sys)
