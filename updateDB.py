#
#
"""
Run this python file in the terminal (located in the main directory) in order to 
create a mongo database, along with the requrired collections for project analysis.
"""

# import libraries
import csv
import pymongo
import pandas as pd
from pathlib import Path

# import dataset file
salary_dataset = pd.read_excel("../Datasets/Player_salary_1990-2017.xlsx")
birthplace_dataset = pd.read_csv("../Datasets/final_heatmap.csv")
yearlyBirthplace_dataset = pd.read_csv("../Datasets/bar_chart_race.csv")
states_df = pd.read_csv('../Datasets/states.csv')

# rename columns to have no spaces 
salary_dataset = salary_dataset.rename(columns={
    'Player Name':'player_name','Salary in $':'salary_$',
    'Season Start':'season_start','Season End':'season_end',
    'Full Team Name':'team_name'})
salary_dataset = salary_dataset.drop(axis=1,columns=['Register Value'])

# establish connection to local host 27017
conn = 'mongodb://localhost:27017'
# connect to MongoClient
client = pymongo.MongoClient(conn)
# begin by dropping any previous version of the MongoDB instance.
client.drop_database('nba_players_db')

# create database by naming db here
db = client.nba_players_db

# create collections and push data from dataset imports

# create salary collection
salary_collection = db.player_salary_info
# use ".to_dict('records')"in combination with .csv variable to create list of dictionaries data set
salary_dataset.reset_index(inplace=True)
salary_dict = salary_dataset.to_dict('records')
# insert data from the 'data_dict' variable into the collection using 'collection' variable
salary_collection.insert_many(salary_dict)

# create birthplace collection
player_birthplace_collection = db.playerBirthplace
# use ".to_dict('records')"in combination with .csv variable to create list of dictionaries data set
birthplace_dataset.reset_index(inplace=True)
birthplace_dict = birthplace_dataset.to_dict('records')
# insert data from the 'data_dict' variable into the collection using 'collection' variable
player_birthplace_collection.insert_many(birthplace_dict)

# create ws/state collection
ws_states_collection = db.ws_states
for index, row in birthplace_dataset.iterrows():
    for i, r in states_df.iterrows():
        if row['Birth_Place'] == r['state']:
            birthplace_dataset.loc[index, 'abreviation'] = r['abr']
# creating an object from the DF
for index, row in birthplace_dataset.iterrows():
    post = {
        'birthplace': row['Birth_Place'],
        'win_shares': row['WS'],
        'long': row['longitude'],
        'lat': row['latitude'],
        'abr' : str(row['abreviation'])
    }
    
    ws_states_collection.insert_one(post)

# create birthplace by year collection
birthplace_by_year_collection = db.yearlyBirthplace
# use ".to_dict('records')"in combination with .csv variable to create list of dictionaries data set
yearlyBirthplace_dataset.reset_index(inplace=True)
yearlyBirthplace_dict = yearlyBirthplace_dataset.to_dict('records')
# insert data from the 'data_dict' variable into the collection using 'collection' variable
birthplace_by_year_collection.insert_many(yearlyBirthplace_dict)

''' 
In order to directly query each collection, visit the mongoDB_upload.ipynb file
in the Code folder and located at the bottom is instructions for querying. 
'''

