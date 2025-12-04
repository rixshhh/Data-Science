import os
import sys
import json
import pandas as pd
import pymongo
import certifi
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from dotenv import load_dotenv

load_dotenv()

MONGO_DB_URL = os.getenv('MONGO_DB_URL')
ca = certifi.where()


class NetworkDataExtract:
    def __init__(self):
        try:
            # Create MongoDB client immediately
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL, tlsCAFile=ca)
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def csv_to_json_converter(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def insert_data_to_mongodb(self, records, database, collection):
        try:
            # Correct database and collection selection
            db = self.mongo_client[database]          # ✔ MongoDB database object
            col = db[collection]                      # ✔ MongoDB collection object

            result = col.insert_many(records)         # ✔ Insert records

            logging.info(f"Inserted {len(result.inserted_ids)} records into MongoDB.")

            return len(result.inserted_ids)

        except Exception as e:
            raise NetworkSecurityException(e, sys)


if __name__ == '__main__':
    FILE_PATH = r'Network_Data\phisingData.csv'
    DATABASE = 'RISHIKESH'
    COLLECTION = 'NetworkData'

    networkobj = NetworkDataExtract()

    records = networkobj.csv_to_json_converter(FILE_PATH)
    print(records)

    inserted_records = networkobj.insert_data_to_mongodb(records, DATABASE, COLLECTION)
    print("No. of records inserted:", inserted_records)
