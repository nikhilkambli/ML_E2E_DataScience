import os
import sys

from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation,DataTransformationConfig
from src.components.model_trainer import ModelTrainingConfig,ModelTrainer

@dataclass
class DataIngestionConfig:
    train_data_path=os.path.join('artifact','train.csv')
    print("path of art"+train_data_path)
    test_data_path=os.path.join('artifact','test.csv')
    raw_data_path=os.path.join('artifact','raw.csv')

class DataIngestion:

    def __init__(self)  :
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info('Data Engestion started')
        try:
            df = pd.read_csv('E:\DataScience_E2E/notebook/data/stud.csv')
            logging.info('Exported read data set')
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            #Saving dataframe to raw file
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info('train test intiated')
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=23)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info('ingestion completed')
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e,sys)
        

if __name__=='__main__':
    obj=DataIngestion()
   
    train_data,test_data=obj.initiate_data_ingestion()
    data_trasnformation=DataTransformation()
    
    train_arr,test_arr,_=data_trasnformation.intitiate_data_transformation(train_data,test_data)

    model_trainer=ModelTrainer()
    print(model_trainer.initiate_model_training(train_arr,test_arr))



