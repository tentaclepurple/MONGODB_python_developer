# Inserting a Document in Python Applications
Review the following code, which demonstrates how to insert a single document and multiple documents into a MongoDB collection by using PyMongo.


## Insert One Document
To insert a single document into a collection, append insert_one() to the collection object. The insert_one() method accepts a document as an argument and returns a result. In this example, we use the result to print the _id value of the inserted document.

In the following code, the document that's being inserted is stored in a variable called new_account. This variable is declared just above the expression that inserts the document.

### Get reference to 'bank' database
db = client.bank

### Get reference to 'accounts' collection
accounts_collection = db.accounts

new_account = {
    "account_holder": "Linus Torvalds",
    "account_id": "MDB829001337",
    "account_type": "checking",
    "balance": 50352434,
    "last_updated": datetime.datetime.utcnow(),
}

### Write an expression that inserts the 'new_account' document into the 'accounts' collection.
result = accounts_collection.insert_one(new_account)

document_id = result.inserted_id
print(f"_id of inserted document: {document_id}")

client.close()

Insert Multiple Documents
To insert more than one document into a collection, append the insert_many() method to the collection object. The insert_many() method accepts an iterable of documents as an argument and returns a result. In this example, we use the result to print out the number of documents inserted and their _id values.

In the following code, the accounts to be inserted are stored in a list variable called new_accounts. This variable is declared just above the expression that inserts the documents.

### Get reference to 'bank' database
db = client.bank

### Get a reference to 'accounts' collection
accounts_collection = db.accounts

new_accounts = [
    {
        "account_id": "MDB011235813",
        "account_holder": "Ada Lovelace",
        "account_type": "checking",
        "balance": 60218,
    },
    {
        "account_id": "MDB829000001",
        "account_holder": "Muhammad ibn Musa al-Khwarizmi",
        "account_type": "savings",
        "balance": 267914296,
    },
]

### Write an expression that inserts the documents in 'new_accounts' into the 'accounts' collection.
result = accounts_collection.insert_many(new_accounts)

document_ids = result.inserted_ids
print("# of documents inserted: " + str(len(document_ids)))
print(f"_ids of inserted documents: {document_ids}")

client.close()
