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

## Insert Multiple Documents
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

------

# Querying a MongoDB Collection in Python Applications
Review the following code, which demonstrates how to query MongoDB collections by using PyMongo.


## Query for a Single Document
To return a single document that matches a query, append find_one() to the collection object. The find_one() method can accept a filter argument that specifies the query to be performed. In this example, the filter is assigned to the document_to_find variable.

find_one() returns the first document that matches the query, or it returns None if there are no matches. In this example, we use the result to print out the returned document.

### Get reference to 'bank' database
db = client.bank

### Get a reference to the 'accounts' collection
accounts_collection = db.accounts

### Query by ObjectId
document_to_find = {"_id": ObjectId("62d6e04ecab6d8e1304974ae")}

### Write an expression that retrieves the document matching the query constraint in the 'accounts' collection.
result = accounts_collection.find_one(document_to_find)
pprint.pprint(result)

client.close()

## Query for Multiple Documents
To return all documents that match a query, append find() to the collection object. The find() method can accept a filter argument that specifies the query to be performed. In this example, the filter is assigned to the documents_to_find variable.

find() returns a Cursor instance, which allows us to iterate over all matching documents. In this example, we use the cursor to print out the documents matched by this query, as well as the total number of documents that are found.

### Get reference to 'bank' database
db = client.bank

### Get a reference to the 'accounts' collection
accounts_collection = db.accounts

### Query
documents_to_find = {"balance": {"$gt": 4700}}

### Write an expression that selects the documents matching the query constraint in the 'accounts' collection.
cursor = accounts_collection.find(documents_to_find)

num_docs = 0
for document in cursor:
    num_docs += 1
    pprint.pprint(document)
    print()
print("# of documents found: " + str(num_docs))

client.close()


-------

# Updating Documents in Python Applications
Review the following code, which demonstrates how to update documents in MongoDB by using PyMongo.


## Update a Single Document
To update a single document that matches a query, append update_one() to the collection object.

The update_one() method has two required parameters: a filter document that matches the document to update, and an update document that specifies the modifications to apply. In this example, the filter is assigned to the document_to_update variable, and the update is assigned to the add_to_balance variable.

update_one() returns a result. In this example, we use the result to print a confirmation of the number of documents that were updated.

We also print the target document before and after the update. This way, we can confirm that the specified modification has been applied.

Here's the code:

### Get reference to 'bank' database
db = client.bank

### Get reference to 'accounts' collection
accounts_collection = db.accounts

### Filter
document_to_update = {"_id": ObjectId("62d6e04ecab6d8e130497482")}

### Update
add_to_balance = {"$inc": {"balance": 100}}

### Print original document
pprint.pprint(accounts_collection.find_one(document_to_update))

### Write an expression that adds to the target account balance by the specified amount.
result = accounts_collection.update_one(document_to_update, add_to_balance)
print("Documents updated: " + str(result.modified_count))

### Print updated document
pprint.pprint(accounts_collection.find_one(document_to_update))

client.close()

##Update Multiple Documents
To update all documents that match a query, append update_many() to the collection object.

The update_many() method also has two required parameters: a filter document that matches the document to update, and an update document that specifies the modifications to apply. In this example, the filter is assigned to the select_accounts variable, and the update is assigned to the set_field variable. Note that in this update, we define a new field and set its initial value.

update_many() returns a result. In this example, we use the result to print out a confirmation of the number of documents that matched and were modified by the operation. We also print out one sample document after the update. This way, we can confirm that the specified modification has been applied.

Here's the code:

### Get reference to 'bank' database
db = client.bank

### Get reference to 'accounts' collection
accounts_collection = db.accounts

### Filter
select_accounts = {"account_type": "savings"}

### Update
set_field = {"$set": {"minimum_balance": 100}}

### Write an expression that adds a 'minimum_balance' field to each savings acccount and sets its value to 100.
result = accounts_collection.update_many(select_accounts, set_field)

print("Documents matched: " + str(result.matched_count))
print("Documents updated: " + str(result.modified_count))
pprint.pprint(accounts_collection.find_one(select_accounts))

client.close()

-------

#  Deleting Documents in Python Applications
Review the following code, which demonstrates how to delete documents in MongoDB by using PyMongo.


## Delete a Single Document
To delete a single document that matches a query, append delete_one() to the collection object.

The delete_one() method has one required parameter, which is a filter that matches the document to delete. In the following example, the filter is assigned to the document_to_delete variable.

Note that if delete_one() is called with an empty query filter document, then it matches and deletes the first document in the collection.

delete_one() returns a result. In this example, we use the result to print the count of documents that were deleted.

We also query for the target document before and after the delete operation as an additional confirmation.

Here's the code:

### Get reference to 'bank' database
db = client.bank

### Get a reference to the 'accounts' collection
accounts_collection = db.accounts

### Filter by ObjectId
document_to_delete = {"_id": ObjectId("62d6e04ecab6d8e130497485")}

### Search for document before delete
print("Searching for target document before delete: ")
pprint.pprint(accounts_collection.find_one(document_to_delete))

### Write an expression that deletes the target account.
result = accounts_collection.delete_one(document_to_delete)

### Search for document after delete
print("Searching for target document after delete: ")
pprint.pprint(accounts_collection.find_one(document_to_delete))

print("Documents deleted: " + str(result.deleted_count))

client.close()

## Delete Multiple Documents
To delete all documents that match a query, append delete_many() to the collection object.

The delete_many() method has one required parameter, which is a filter document that matches the document to delete. In the following example, the filter is assigned to the documents_to_delete variable.

Note that if we call delete_many() with an empty query filter document, then all documents in the collection will be deleted.

delete_many() returns a result. In this example, we use the result to print the count of documents that were deleted.

We also query for a sample target document before and after the delete operation as an additional confirmation.

Here's the code:

### Get reference to 'bank' database
db = client.bank

### Get a reference to the 'accounts' collection
accounts_collection = db.accounts

### Filter for accounts with balance less than $2000
documents_to_delete = {"balance": {"$lt": 2000}}

### Search for sample document before delete
print("Searching for sample target document before delete: ")
pprint.pprint(accounts_collection.find_one(documents_to_delete))

### Write an expression that deletes the target accounts.
result = accounts_collection.delete_many(documents_to_delete)

### Search for sample document after delete
print("Searching for sample target document after delete: ")
pprint.pprint(accounts_collection.find_one(documents_to_delete))

print("Documents deleted: " + str(result.deleted_count))

client.close()
