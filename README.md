# NBA Analysis Project
* Group Members: Charles Hedeen, Daniel Carter, Franklin Truong, Jarrod Williams and Rob Savage.
    * Website available through link at the top right of the page OR clone the main repo and follow instructions below.
    * <strong>All analysis is provided via our deployed [website!](https://nba-winshare-analysis.herokuapp.com/)</strong>

## Questions:

* Which states in the USA have the highest total career Win Shares (produced by players from those states)?
* How has the average NBA salary changed overtime? 1990-2017
* How has the diversity of the NBA players changed overtime?

## Tasks

* Visualizations (JS & Python) 
* Data Cleaning and Aggregation 
* Database/ETL 
* Flask/API 
* HTML/CSS 
* New Javascript Library:
  * High Charts

## Installing required packages
* 'requirements.txt' file is located in the root of the repo. Open a terminal window from the root of the repo and run (this will add all necessary libraries and versions):
  * $ pip install -r requirements.txt

## Using MongoDB

Database creation code located in 'MongoDB_upload.ipynb', if run from beginning to end, the code will create a Mongo database on your local machine which will allow you to analyze the data independently.

### Steps to create database on local machine (outlined in the code as well):
* Be sure you have MongoDB installed on your machine
  * Open your machines terminal and run Mongodb-community
  * In a new terminal window, run the command 'mongo' to initiate MongoDB
  * Keep both terminal windows open while using mongo!
* Open the 'MongoDB Compass Community App' and click the 'Connect' button
* In the repository folder you have cloned to your machine, open Jupyter Notebook by typing 'jupyter notebook' into the command line. Verify you are in the correct directory.
* In Jupyter Notebook, navigate to the 'MongoDB_upload.ipynb' notebook
* Inside 'MongoDB_upload.ipynb', run the entire Kernel by clicking on the play button in the ribbon bar at the top of the window.
* Navigate back to the 'MongoDB Compass Community App' and click the refresh button in the top left corner
* You should now see a database titled 'nba_players_db' and within that database, and five total collection.

### Querying the database:
* Basic querying code is available in the 'MongoDB_upload.ipynb' notebook at the bottom of the page. You will find a code block within the file that outlines how to query specific fields and values within jupyter notebook. 

## Running Flask App
* The python Flask app is located in the folder called "Flask_app"
* Open a terminal inside this folder and run the command (which will launch the app):
  * $ python simple_app.py
* click on the link in the terminal to open the server in your browser (LINK: 'http://127.0.0.1:5000/').
* Stop running the Flask app by pressing ctrl+c in the terminal.

## API
* Each API page can be found within the drop down menu at the top of our websites home page.

## Source citations:
* Player Salary Data:
  https://data.world/datadavis/nba-salaries/workspace/file?filename=nba_salaries_1990_to_2018.csv 
* Player Birthplace Data:
  https://www.kaggle.com/drgilermo/nba-players-stats/data 
* Player Win Share:
  https://www.basketball-reference.com/leagues
* State abbreviation: 
  https://worldpopulationreview.com/states/state-abbreviations
