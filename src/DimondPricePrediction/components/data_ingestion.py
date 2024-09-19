import pandas as pd
import numpy as np
import os
import sys
from src.DimondPricePrediction.exception import customexception
from src.DimondPricePrediction.logger import logging

from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path


class DataIngestionConfig:
    raw_data_path:str=os.path.join("artifacts","raw.csv")
    train_data_path:str=os.path.join("artifacts","train1.csv")
    test_data_path:str=os.path.join("artifacts","test.csv")





class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data Ingestion started")


        try:
            data=pd.read_csv(Path(os.path.join("notebooks/data","train.csv")))
            logging.info("Data has read")



            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)),exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info("I have saved raw data in artifact folder ")

            
            logging.info("train_test_split has started")
            
            train_data,test_data=train_test_split(data,test_size=0.25)
            
            logging.info("train_test_split has completed")

            train_data.to_csv(self.ingestion_config.train_data_path,index=False)
            test_data.to_csv(self.ingestion_config.test_data_path,index=False)

            logging.info("Data ingestion part completed")


        except Exception as e:
            logging.info("excpetion occured during the data ingestion ")
            raise customexception(e,sys)



    