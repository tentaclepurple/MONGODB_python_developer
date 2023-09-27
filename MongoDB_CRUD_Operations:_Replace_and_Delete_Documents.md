MongoDB CRUD Operations: Replace and Delete Documents

#Replacing a Document in MongoDB
To replace documents in MongoDB, we use the replaceOne() method. The replaceOne() method takes the following parameters:

filter: A query that matches the document to replace.
replacement: The new document to replace the old one with.
options: An object that specifies options for the update.
In the previous video, we use the _id field to filter the document. In our replacement document, we provide the entire document that should be inserted in its place. Here's the example code from the video:

db.books.replaceOne(
  {
    _id: ObjectId("6282afeb441a74a98dbbec4e"),
  },
  {
    title: "Data Science Fundamentals for Python and MongoDB",
    isbn: "1484235967",
    publishedDate: new Date("2018-5-10"),
    thumbnailUrl:
      "https://m.media-amazon.com/images/I/71opmUBc2wL._AC_UY218_.jpg",
    authors: ["David Paper"],
    categories: ["Data Science"],
  }
)

#Updating MongoDB Documents by Using updateOne()
The updateOne() method accepts a filter document, an update document, and an optional options object. MongoDB provides update operators and options to help you update documents. In this section, we'll cover three of them: $set, upsert, and $push.

$set
The $set operator replaces the value of a field with the specified value, as shown in the following code:

db.podcasts.updateOne(
  {
    _id: ObjectId("5e8f8f8f8f8f8f8f8f8f8f8"),
  },

  {
    $set: {
      subscribers: 98562,
    },
  }
)
upsert
The upsert option creates a new document if no documents match the filtered criteria. Here's an example:

db.podcasts.updateOne(
  { title: "The Developer Hub" },
  { $set: { topics: ["databases", "MongoDB"] } },
  { upsert: true }
)
$push
The $push operator adds a new value to the hosts array field. Here's an example:

db.podcasts.updateOne(
  { _id: ObjectId("5e8f8f8f8f8f8f8f8f8f8f8") },
  { $push: { hosts: "Nic Raboy" } }
)
