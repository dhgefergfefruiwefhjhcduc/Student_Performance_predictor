print("THIS IS data_ingestion.py")
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import os
import sys
from src.exception import CustomException
from src.logger import logging
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig
from dataclasses import dataclass

class DataIngestionConfig:
    train_data_path=os.path.join("artifacts","train_data.csv")
    test_data_path=os.path.join("artifacts","test_data.csv")
    raw_data_path=os.path.join("artifacts","raw_data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestionconfig=DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info("Entered to Data Ingestion")
        try:
            df=pd.read_csv("data\StudentsPerformance.csv")
            logging.info("Reading the dataset as dataframe")
            os.makedirs(os.path.dirname(self.ingestionconfig.train_data_path),exist_ok=True)
            df.to_csv(self.ingestionconfig.raw_data_path,index=False,header=True)
            train_set,test_set=train_test_split(df,test_size=0.3,random_state=42)
            logging.info("Started Train Test Split")
            train_set.to_csv(self.ingestionconfig.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestionconfig.test_data_path,index=False,header=True)
            logging.info("Train and Test  data are saved successfully")
            return (
                self.ingestionconfig.train_data_path,self.ingestionconfig.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)

if __name__=="__main__":
    print("Starting data ingestion...")
    obj = DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

    
