import pandas as pd
import numpy as np
import os
import sys

from dataclasses import dataclass
from src.DimondPricePrediction.exception import customexception
from src.DimondPricePrediction.logger import logging


from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder,StandardScaler


from src.DimondPricePrediction.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join("artifacrs","preprocessor.pkl")



class DataTransoformation:
    def __init__(self):
        self.data_tranformation_config=DataTransformationConfig()

    def get_data_tranformation(self):
        try:
            logging.info("Data transformation initiated")
            
        except Exception as e:
            logging.info("Exception occured in the get_data_transmation")

            raise customexception(e,sys)




    def initialize_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            logging.info("read train and test data complete ")
            logging.info(f'Train Dataframe Head : \n{train_df.head().to_string()}')
            logging.info(f'Test Dataframe Head : \n{test_df.head().to_string()}')

            preprocessing_obj=self.get_data_tranformation()
       
        except Exception as e:
            logging.info("Exception occured during the Initialize_data_tranformation")
            raise customexception(e,sys)

    