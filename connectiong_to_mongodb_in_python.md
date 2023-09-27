
crear entorno
python3 -m venv nombre_del_entorno
source mi_entorno/bin/activate


pip install pymongo

touch connection.py
from pymongo import MongoClient

mongo_uri = "mongodb+srv://admin:purpletentacle2023@clustertest.xxaefyu.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(mongo_uri)

for i in client.list_database_names():
	print(i)

Troubleshooting a MongoDB Connection in Python Applications
Review the following steps, which demonstrate how to add your current IP address to the IP Access List in Atlas. Updating your IP address can help you troubleshoot connection issues.


Steps

Log in to Atlas. The login page looks like the following: 
![image](https://github.com/tentaclepurple/MongoDB_python_developer/assets/116112114/34fbfa87-f3fa-4f30-aed8-f00694f58dc2)



Once you're logged in, you will be taken to the Atlas dashboard for your current project. Click "Network Access." 

![image](https://github.com/tentaclepurple/MongoDB_python_developer/assets/116112114/267f7c3e-b435-4d88-ab7f-629cc1a7e3df)


Click the “Add IP Address” button. 

![image](https://github.com/tentaclepurple/MongoDB_python_developer/assets/116112114/674c36a1-bac2-4cd1-8911-47185571dc4b)


Select "Add Current IP Address," and then click the Confirm button. 
![image](https://github.com/tentaclepurple/MongoDB_python_developer/assets/116112114/b3a025a8-0a47-4b6d-91b4-3f5df017c0c4)
