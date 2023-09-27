
crear entorno
python3 -m venv nombre_del_entorno
source mi_entorno/bin/activate


pip install pymongo

touch connection.py
from pymongo import MongoClient

mongo_uri = "mongodb+srv://admin:purpletentacle2023@clustertest.xxaefyu.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(mongo_uri)

for i in client.list_database_names():
	print(i)

