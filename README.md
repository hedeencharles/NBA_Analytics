# group_project2
    * Use 'virtualenv' to install requrired packages from 'requirements.txt' to run application.
NBA analytics

# PROJECT PROPOSAL

## Questions:

* Is there a correlation between a player's birthplace and NBA success?
* Have the total number or ratio of foreign players increased since the formation of the NBA?
* Does the regular season win share metric correlate to playoff success?
* Do load management techniques correlate to playoff success?

## Tasks

* Visualizations (JS & Python) - Rob Savage
* Data Cleaning and Aggregation - Franklin Truong
* Database/ETL - Charles Hedeen
* Flask/API - Jarrod Williams
* HTML/CSS - Daniel Carter
* New Javascript Library:
  * High Charts

## Using MongoDB

Database creation code located in 'MongoDB_upload.ipynb', if run from beginning to end, the code will create a Mongo database on your local machine which will allow you to analyze the data independently.

### Steps to create database on local machine (outlined in the code as well):
* Be sure you have MongoDB installed on your machine
  * Open your machines terminal and run Mongodb-community
  * In a new terminal window, run the command 'mongo' to initiate MongoDB
  * Keep both terminal windows open while using mongo!
* Open the 'MongoDB Compass Community App' and click the 'Connect' button
<!-- ![MongoDB Compass Community App Home Page](/Readme_files/Images/MongoDB_Home_Screen.png) -->
* In the repository folder you have cloned to your machine, open Jupyter Notebook by typing 'jupyter notebook' into the command line. Verify you are in the correct directory.
* In Jupyter Notebook, navigate to the 'MongoDB_upload.ipynb' notebook
* Inside 'MongoDB_upload.ipynb', run the Kernel (If you want to run cell by cell, click into the top cell and click SHIFT + ENTER down the entire list of cells)
* Navigate back to the 'MongoDB Compass Community App' and click the refresh button in the top left corner
<!-- ![Refresh DB List](/Readme_files/Images/Refresh_DB_List.png) -->
* You should now see a database titled '  final_testing_beds_db' and within that database, a collection titled 'testing_beds', and a list of documents as shown below
<!-- ![Final Data Display](/Readme_files/Images/Final_Data_Display.png) -->

### Querying the database:
* Basic querying code is available in the 'MongoDB_upload.ipynb' notebook. You will find a code block within the file that outlines how to query specific field values.