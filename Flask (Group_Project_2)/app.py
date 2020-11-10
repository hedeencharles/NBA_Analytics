import os
from flask import Flask, render_template, redirect, url_for, jsonify, request
from flask import render_template
from flask_pymongo import PyMongo
# import updateDB
from flask_cors import CORS



#create the Flask app
app = Flask(__name__)
CORS(app)

# setup mongo db connection
app.config["DEBUG"] = True

# app.config["MONGO_URI"] = "mongodb://localhost:27017/nba_players_db"
app.config["MONGO_URI"] = os.environ['MONGO_URI'] 
mongo = PyMongo(app)

# create variables for collections
states_collection = mongo.db.ws_states
player_salary_collection = mongo.db.player_salary_info
player_birthplace_collection = mongo.db.playerBirthplace
yearlyBirthplace_collection = mongo.db.yearlyBirthplace

#Create the Flask route for the index page
@app.route('/')
def index():
    return render_template("index.html")

# 
# 
# @app.route('/bar_race')
# def barRace():
#     return render_template("bar_race.html")

# state abbreviation and win shares
@app.route('/api/states_winshare')
def states_winshare():
    data = list(states_collection.find({ }, { '_id': 0}))
    consolidated_data = []
    for x in data:
        if not x['abr'] == 'nan':
            obj = {
            'value': round(x['win_shares']),
            'code': x['abr']
            }
            if obj['value'] == 0:
                obj['value'] = 0.1

            consolidated_data.append(obj)

    return jsonify(consolidated_data)


# player salary api
@app.route('/api/player_salary')
def salary_player():
    return jsonify(list(player_salary_collection.find({ },
   { '_id': 0})))

# player salary api
@app.route('/api/player_birthplace')
def player_birthplace():
    return jsonify(list(player_birthplace_collection.find({ },
   { '_id': 0})))

# yearly birthplace api
@app.route('/api/yearly_birthplace')
def yearly_birthplace():
    return jsonify(list(yearlyBirthplace_collection.find({ },
   { '_id': 0})))

if __name__ == "__main__":
    app.run(debug=True)

