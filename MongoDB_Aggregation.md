# Introduction to MongoDB Aggregation
This section contains key definitions for this lesson, as well as the code for an aggregation pipeline.

Definitions
Aggregation: Collection and summary of data

Stage: One of the built-in methods that can be completed on the data, but does not permanently alter it

Aggregation pipeline: A series of stages completed on the data in order

### Structure of an Aggregation Pipeline
    db.collection.aggregate([
                {
                $stage1: {
                    { expression1 },
                    { expression2 }...
                },
                $stage2: {
                    { expression1 }...
                }
            }
        ])

# Using $match and $group Stages in a MongoDB Aggregation Pipeline
Review the following sections, which show the code for the $match and $group aggregation stages.

## $match
The $match stage filters for documents that match specified conditions. Here's the code for $match:

    {
      $match: {
         "field_name": "value"
      }
    }
## $group
The $group stage groups documents by a group key.

    {
      $group:
        {
          _id: <expression>, // Group key
          <field>: { <accumulator> : <expression> }
        }
     }
## $match and $group in an Aggregation Pipeline
The following aggregation pipeline finds the documents with a field named "state" that matches a value "CA" and then groups those documents by the group key "$city" and shows the total number of zip codes in the state of California.

    db.zips.aggregate([
    {   
       $match: { 
          state: "CA"
        }
    },
    {
       $group: {
          _id: "$city",
          totalZips: { $count : { } }
       }
    }
    ])

# Using $sort and $limit Stages in a MongoDB Aggregation Pipeline
Review the following sections, which show the code for the $sort and $limit aggregation stages.

### $sort
The $sort stage sorts all input documents and returns them to the pipeline in sorted order. We use 1 to represent ascending order, and -1 to represent descending order.

    {
        $sort: {
            "field_name": 1
        }
    }


### $limit
The $limit stage returns only a specified number of records.

    {
      $limit: 5
    }


### $sort and $limit in an Aggregation Pipeline
The following aggregation pipeline sorts the documents in descending order, so the documents with the greatest pop value appear first, and limits the output to only the first five documents after sorting.

    db.zips.aggregate([
    {
      $sort: {
        pop: -1
      }
    },
    {
      $limit:  5
    }
    ])
