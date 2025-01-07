from params import *
import random

def insert_user(db):

    for i in range(0, 5):
        user = {
                    "username": f"user{i}",
                    "age": random.randint(18, 70),
                    "city": random.choice(city),
                    "curses": {
                        "piscine": {
                            "year": random.randint(2002, 2025),
                            "projects": [
                                {"project_name": proj, "grade": random.randint(50, 100)}
                                for proj in random.sample(
                                        piscine_projects,
                                        random.randint(1, len(piscine_projects))
                                )
                            ]
                        },
                        "cursus": {
                            "year": random.randint(2002, 2025),
                            "projects": [
                                {"project_name": proj, "grade": random.randint(50, 100)}
                                for proj in random.sample(
                                        cursus_projects,
                                        random.randint(1, len(cursus_projects))
                                )
                            ]
                        }
                    }
                }
        result = db.users.insert_one(user)
        print("doc ID:", result.inserted_id)


def delete(db):
    result = db.users.delete_many({})


def find_one(db, query):
    result = db.users.find_one(query)
    return result


def find(db, query):
    result = db.users.find(query)
    return result

