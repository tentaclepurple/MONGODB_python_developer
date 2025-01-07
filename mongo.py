import ops
from connect import connect
import time
import pprint
from bson import ObjectId


if __name__ == "__main__":
    client = connect()

    db = client.test_db

    db.users.create_index("name")

    start_time = time.time()

    #query = {'_id': ObjectId('677c586b032669ccfc80f737')}
    query = {"curses.cursus.projects": 
                {'$elemMatch': 
                    {"project_name": "push_swap"}}}



    #ops.insert_user(db)
    #ops.delete(db)
    result = ops.find(db, query)
    #result = ops.find_one(db, query)
    for doc in result:
        print(doc["username"])
    #pprint.pprint(result)

    client.close()

    end_time = time.time()
    print(f"Total time: {(end_time - start_time):.5f}")


    

    



