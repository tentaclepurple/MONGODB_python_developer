
# Multi-Document Transactions
ACID transactions in MongoDB are typically used only by applications where values are exchanged between different parties, such as banking or business applications. If you find yourself in a scenario where a multi-document transaction is required, it's very likely that you will complete a transaction with one of MongoDB's drivers. For now, let's focus on completing and canceling multi-document transactions in the shell to become familiar with the steps.


Using a Transaction: Video Code
Here is a recap of the code that's used to complete a multi-document transaction:

    const session = db.getMongo().startSession()

    session.startTransaction()

const account = session.getDatabase('< add database name here>').getCollection('<add collection name here>')

//Add database operations like .updateOne() here

    session.commitTransaction()

Aborting a Transaction
If you find yourself in a scenario that requires you to roll back database operations before a transaction is completed, you can abort the transaction. Doing so will roll back the database to its original state, before the transaction was initiated.


Aborting a Transaction: Video Code
Here is a recap of the code that's used to cancel a transaction before it completes:

    const session = db.getMongo().startSession()

    session.startTransaction()
    
    const account = session.getDatabase('< add database name here>').getCollection('<add collection name here>')
    
    //Add database operations like .updateOne() here
    
    session.abortTransaction()
