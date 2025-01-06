from connect import connect
from pymongo import MongoClient



if __name__ == "__main__":
    client = connect()

    db = client["test_db"]

    document = {"name": "TesUSer", "age": 30, "city": "Madrid"}
    
    result = db.users.insert_one(document)

    print("doc ID:", result.inserted_id)