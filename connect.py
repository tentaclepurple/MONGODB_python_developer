from dotenv import load_dotenv
from pymongo import MongoClient
import os


load_dotenv()


def connect():
    MONGO_URI = os.getenv('ATLAS_URI')
    print(MONGO_URI)
    client = MongoClient(MONGO_URI)
    return client