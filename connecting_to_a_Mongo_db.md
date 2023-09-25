
Locate the MongoDB Connection String
In this lesson, you will go through the steps to locate the MongoDB connection string within the Atlas dashboard.

Instructions
![image](https://github.com/tentaclepurple/MongoDB_python_developer/assets/116112114/444e56d0-ec3d-45d4-864d-1c4b5148f46f)


Go to https://account.mongodb.com/account/login and log in to Atlas. The login page should look like the following:

![image](https://github.com/tentaclepurple/MongoDB_python_developer/assets/116112114/3ae74896-d424-4ff4-b4ce-1857de44981b)

Once logged in, you will be taken to the Atlas dashboard for your current project, as shown in the following screenshot: 
![image](https://github.com/tentaclepurple/MongoDB_python_developer/assets/116112114/12db750f-ac35-457f-988d-9fcf7e81ddda)


Click the Connect button. 

![image](https://github.com/tentaclepurple/MongoDB_python_developer/assets/116112114/bd399835-51bd-4cb0-bea9-d6d522ff1a6c)

This should open a new window, which shows options for connecting to your cluster. Click the "Connect your application" button. 
![image](https://github.com/tentaclepurple/MongoDB_python_developer/assets/116112114/c4f9149b-7fd5-454c-9265-422314b6c4d0)


After clicking the button, you will be taken to the following window: 
![image](https://github.com/tentaclepurple/MongoDB_python_developer/assets/116112114/0718b680-a76f-4f16-bc3a-623d8034de52)


Click the copy icon to copy your connection string. 
![image](https://github.com/tentaclepurple/MongoDB_python_developer/assets/116112114/e49c78a1-d3c8-4ad5-a76d-787841f05a1f)

Now you can use your connection string to connect to your Atlas cluster!



COMPASS

Install MongoDB Compass
In this lesson, you will learn how to install MongoDB Compass on your operating system.

The lesson contains the following sections:

Install MongoDB Compass
Install MongoDB Compass on Windows
Compass Requirements
Download Instructions
Installation Instructions
Install MongoDB Compass on macOS
Compass Requirements
Download Instructions
Installation Instructions

Install MongoDB Compass on Windows
Compass Requirements
Compass requires:

64-bit version of Microsoft Windows 7 or later

MongoDB 3.6 or later

Microsoft .NET Framework version 4.5 or later. Note that the Compass installer prompts you to install the minimum required version of the .NET framework if it's not already installed on your system.

Starting the installation as an administrator if you are running a silent installation by using Microsoft PowerShell


Download Instructions


Go to https://www.mongodb.com/try/download/compass and locate MongoDB Compass, as shown in the following screenshot: 
![image](https://github.com/tentaclepurple/MongoDB_python_developer/assets/116112114/6fe5d55a-906a-4013-bb5e-09ad8a7b3a8c)

Select the installer you prefer. The MongoDB Compass installer is available as a .exe or .msi package or a .zip archive.


Click the Download button. 
![image](https://github.com/tentaclepurple/MongoDB_python_developer/assets/116112114/6182a8c8-6309-468f-877b-2bf11c47d502)


Installation Instructions

Double-click the installer file.

Follow the prompts to install Compass. You can select the destination of the Compass installation.


Install MongoDB Compass on macOS
Compass Requirements
Compass requires:

64-bit version of macOS 10.12 or later

MongoDB 3.6 or later


Download Instructions


Go to https://www.mongodb.com/try/download/compass and locate MongoDB Compass, as shown in the following screenshot: 

Download the latest version of MongoDB Compass for macOS. The MongoDB Compass installer is a .dmg disk image.
Click the Download button. 




Installation Instructions


Double-click the .dmg file to open the disk image within the macOS Finder.

Drag the MongoDB Compass application to your Applications folder.

Eject the disk image.

From the Applications folder, double-click the Compass icon to start the application.

When you open MongoDB Compass for the first time, you may receive a notice stating that it is an application downloaded from the internet, requiring you to confirm you want to open it. Click Open to continue and launch Compass.



Connect to an Atlas Cluster with MongoDB Compass
In this lab, you will connect to your Atlas cluster by using MongoDB Compass and a connection string.


Directions
Follow these steps:


Sign in to your MongoDB Atlas account at https://www.mongodb.com/atlas/database.

Once logged in, click the Connect button. 

![image](https://github.com/tentaclepurple/MongoDB_python_developer/assets/116112114/7d45c4f9-93ae-4e22-a9ae-71c9326ad10e)


Click the "Connect using MongoDB Compass" button. 

![image](https://github.com/tentaclepurple/MongoDB_python_developer/assets/116112114/92cf7ead-1313-4434-a864-4fd9f50bdf05)


Click the copy icon to copy your Atlas cluster connection string, as shown in the following screenshot: 


![image](https://github.com/tentaclepurple/MongoDB_python_developer/assets/116112114/8af8acc7-38af-42a1-af10-29ddc640e641)

Open MongoDB Compass and select New Connection. 

![image](https://github.com/tentaclepurple/MongoDB_python_developer/assets/116112114/242ea08f-f5f1-4c77-9868-72ec7633c4ef)


Paste in your connection string, which should be similar to the following:
mongodb+srv://MDBUser:<password>@mdb-training-cluster.swnn5.mongodb.net/test

![image](https://github.com/tentaclepurple/MongoDB_python_developer/assets/116112114/7da3ef78-43e6-4422-a24e-8f1046c55543)



Click the Connect button.  
