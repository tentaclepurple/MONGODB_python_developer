# Using MongoDB Aggregation Stages with Python: $match and $group
Review the following code, which demonstrates how to use the $match and $group stages in a MongoDB aggregation pipeline by using PyMongo.


### Using $match
When we build queries by using the aggregation framework, each stage transforms or organizes data in a specific way. In this lesson, we used the $match and $group stages.

Use the $match operator to select documents that match the specified query condition(s) and pass the matching documents to the next stage. $match takes a document that specifies the query.

$match should be placed early in a pipeline to reduce the number of documents that will be processed later in the pipeline.

Here's an example of the $match stage:

  # Select accounts with balances of less than $1000.
  select_by_balance = {"$match": {"balance": {"$lt": 1000}}}

### Using $group
Use the $group stage to separate documents into groups. The $group stage must have an _id field that specifies the group key. The group key is preceded by a $ and enclosed in quotation marks.

A $group stage can include additional field(s) that are computed by using accumulator operators, such as $avg.

Here's an example of the $group stage:

  # Separate documents by account type and calculate the average balance for each account type.
  separate_by_account_calculate_avg_balance = {
      "$group": {"_id": "$account_type", "avg_balance": {"$avg": "$balance"}}
  }

Aggregation Example That Uses $match and $group
The following is an example of an aggregation pipeline that uses $match and $group.

  # Connect to MongoDB cluster with MongoClient
  client = MongoClient(MONGODB_URI)

  # Get reference to 'bank' database
  db = client.bank
  
  # Get reference to 'accounts' collection
  accounts_collection = db.accounts
  
  # Calculate the average balance of checking and savings accounts with balances of less than $1000.
  
  # Select accounts with balances of less than $1000.
  select_by_balance = {"$match": {"balance": {"$lt": 1000}}}
  
  # Separate documents by account type and calculate the average balance for each account type.
  separate_by_account_calculate_avg_balance = {
      "$group": {"_id": "$account_type", "avg_balance": {"$avg": "$balance"}}
  }

  # Create an aggegation pipeline using 'stage_match_balance' and 'stage_group_account_type'.
  pipeline = [
      select_by_balance,
      separate_by_account_calculate_avg_balance,
  ]
  
  # Perform an aggregation on 'pipeline'.
  results = accounts_collection.aggregate(pipeline)
  
  print()
  print(
      "Average balance of checking and savings accounts with balances of less than $1000:", "\n"
  )
  
  for item in results:
      pprint.pprint(item)
  
  client.close()
