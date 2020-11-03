# group_project2
* Group Members: Charles Hedeen, Franklin Truong, Jarrod Williams and Rob Savage.
    * Use 'virtualenv' to install requrired packages from 'requirements.txt' to run application.

# PROJECT PROPOSAL

## Questions:

* Which states in the USA have the highest total career Win Shares (produced by players from those states)?
* How has the average NBA salary changed overtime? 1990-2017
* How has the diversity of the NBA players changed overtime?

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
* Inside 'MongoDB_upload.ipynb', run the entire Kernel by clicking on the play button in the ribbon bar at the top of the window.
* Navigate back to the 'MongoDB Compass Community App' and click the refresh button in the top left corner
<!-- ![Refresh DB List](/Readme_files/Images/Refresh_DB_List.png) -->
* You should now see a database titled 'nba_players_db' and within that database, and five total collection.
<!-- ![Final Data Display](/Readme_files/Images/Final_Data_Display.png) -->

### Querying the database:
* Basic querying code is available in the 'MongoDB_upload.ipynb' notebook at the bottom of the page. You will find a code block within the file that outlines how to query specific fields and values within jupyter notebook. 

## API
* Each API page we created can be found within the drop down menu at the top of our websites home page.

## Source citations:
* Player Salary Data:
  https://data.world/datadavis/nba-salaries/workspace/file?filename=nba_salaries_1990_to_2018.csv 
* Player Birthplace Data:
  https://www.kaggle.com/drgilermo/nba-players-stats/data 
* Player Win Share:
  https://www.basketball-reference.com/leagues
* State abreviation: 
  https://worldpopulationreview.com/states/state-abbreviations


  