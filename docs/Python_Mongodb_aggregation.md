# Using MongoDB Aggregation Stages with Python: $match and $group
Review the following code, which demonstrates how to use the $match and $group stages in a MongoDB aggregation pipeline by using PyMongo.


### Using $match
When we build queries by using the aggregation framework, each stage transforms or organizes data in a specific way. In this lesson, we used the $match and $group stages.

Use the $match operator to select documents that match the specified query condition(s) and pass the matching documents to the next stage. $match takes a document that specifies the query.

$match should be placed early in a pipeline to reduce the number of documents that will be processed later in the pipeline.

Here's an example of the $match stage:

    #Select accounts with balances of less than $1000.
    select_by_balance = {"$match": {"balance": {"$lt": 1000}}}

### Using $group
Use the $group stage to separate documents into groups. The $group stage must have an _id field that specifies the group key. The group key is preceded by a $ and enclosed in quotation marks.

A $group stage can include additional field(s) that are computed by using accumulator operators, such as $avg.

Here's an example of the $group stage:

    #Separate documents by account type and calculate the average balance for each account type.
    separate_by_account_calculate_avg_balance = {
        "$group": {"_id": "$account_type", "avg_balance": {"$avg": "$balance"}}
    }

Aggregation Example That Uses $match and $group
The following is an example of an aggregation pipeline that uses $match and $group.

    #Connect to MongoDB cluster with MongoClient
    client = MongoClient(MONGODB_URI)
  
    # Get reference to 'bank' database
    db = client.bank
    
    #Get reference to 'accounts' collection
    accounts_collection = db.accounts
    
    #Calculate the average balance of checking and savings accounts with balances of less than $1000.
    
    #Select accounts with balances of less than $1000.
    select_by_balance = {"$match": {"balance": {"$lt": 1000}}}
    
    #Separate documents by account type and calculate the average balance for each account type.
    separate_by_account_calculate_avg_balance = {
        "$group": {"_id": "$account_type", "avg_balance": {"$avg": "$balance"}}
    }
  
    #Create an aggegation pipeline using 'stage_match_balance' and 'stage_group_account_type'.
    pipeline = [
        select_by_balance,
        separate_by_account_calculate_avg_balance,
    ]
    
    #Perform an aggregation on 'pipeline'.
    results = accounts_collection.aggregate(pipeline)
    
    print()
    print(
        "Average balance of checking and savings accounts with balances of less than $1000:", "\n"
    )
    
    for item in results:
        pprint.pprint(item)
    
    client.close()

-----

# Using MongoDB Aggregation Stages with Python: $sort and $project
Review the following code, which demonstrates how to use the $sort and $project stages in a MongoDB aggregation pipeline by using PyMongo.


### Using $sort
When we build queries by using the aggregation framework, each stage transforms or organizes data in a specific way. In this lesson, we focused on the $sort and $project stages.

Use the $sort operator to organize the input documents in ascending or descending order. $sort takes a document that specifies the field(s) to sort by and the respective sort order. To sort in ascending order, use the value of 1. For descending order, use the value of -1.

Here's an example of a $sort stage:

    # Organize documents in order from highest balance to lowest.
    organize_by_original_balance = {"$sort": {"balance": -1}}

### Using $project
Use the $project stage to specify the fields returned by the aggregation. $project can be used to include or exclude existing fields by setting a field to 1 to include or 0 to exclude. It can also be used to add new fields or reset the value of existing fields.

To add a new field by using $project, specify the field name and set its value to an expression like this: <field>: <expression>. In this example, the new field name is gbp_balance. The expression contains the $divide arithmetic operator, the $balance field reference, and the conversion_rate_usd_to_gbp variable.

When creating an aggregation pipeline, the $project stage should usually be the last stage in a pipeline because it specifies the exact fields to be returned to the client.

Here's an example of a $project stage:

    # Return only the account type & balance fields, plus a new field containing balance in Great British Pounds (GBP).
    return_specified_fields = {
        "$project": {
            "account_type": 1,
            "balance": 1,
            "gbp_balance": {"$divide": ["$balance", conversion_rate_usd_to_gbp]},
            "_id": 0,
        }
    }

Aggregation Example That Uses $match, $sort, and $project
The following is an example of an aggregation pipeline that uses $match, $sort, and $project:

    # Connect to MongoDB cluster with MongoClient
    client = MongoClient(MONGODB_URI)
    
    # Get reference to 'bank' database
    db = client.bank
    
    # Get a reference to the 'accounts' collection
    accounts_collection = db.accounts
    
    # Return the account type, original balance, and balance converted to Great British Pounds (GBP)
    # of all checking accounts with an original balance of greater than $1,500 US dollars, in order from highest original balance to lowest.
    
    # To calculate the balance in GBP, divide the original balance by the conversion rate
    conversion_rate_usd_to_gbp = 1.3
    
    # Select checking accounts with balances of more than $1,500.
    select_accounts = {"$match": {"account_type": "checking", "balance": {"$gt": 1500}}}
    
    # Organize documents in order from highest balance to lowest.
    organize_by_original_balance = {"$sort": {"balance": -1}}
    
    # Return only the account type & balance fields, plus a new field containing balance in Great British Pounds (GBP).
    return_specified_fields = {
        "$project": {
            "account_type": 1,
            "balance": 1,
            "gbp_balance": {"$divide": ["$balance", conversion_rate_usd_to_gbp]},
            "_id": 0,
        }
    }
    
    # Create an aggegation pipeline containing the four stages created above
    pipeline = [
        select_accounts,
        organize_by_original_balance,
        return_specified_fields,
    ]
    
    # Perform an aggregation on 'pipeline'.
    results = accounts_collection.aggregate(pipeline)
    
    print(
        "Account type, original balance and balance in GDP of checking accounts with original balance greater than $1,500,"
        "in order from highest original balance to lowest: ", "\n"
    )
    
    for item in results:
        pprint.pprint(item)
    
    client.close()
