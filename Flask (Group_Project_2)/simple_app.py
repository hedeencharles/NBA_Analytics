from flask import Flask, render_template, redirect, url_for, jsonify, request
from flask import render_template
from flask_pymongo import PyMongo
# from flask_cors import CORS


#create the Flask app
app = Flask(__name__)
# CORS(app)

# setup mongo db connection
app.config["DEBUG"] = True

app.config["MONGO_URI"] = "mongodb://localhost:27017/nba_players_db"
mongo = PyMongo(app)

# create variables for collections
ws_birthplace_collection = mongo.db.WSbirthplace
ws_player_collection = mongo.db.playerWS
player_salary_collection = mongo.db.player_salary_info
player_birthplace_collection = mongo.db.playerBirthplace


#Create the Flask route for the index page
@app.route('/')
def index():
    return render_template("index.html")

# birthplace api
@app.route('/api/ws_birthplace')
def ws_birthplace():
    return jsonify(list(ws_birthplace_collection.find({ },
   { '_id': 0})))

# player salary api
@app.route('/api/player_salary')
def salary_player():
    return jsonify(list(player_salary_collection.find({ },
   { '_id': 0})))

# player salary api
@app.route('/api/player_ws')
def ws_player():
    return jsonify(list(ws_player_collection.find({ },
   { '_id': 0})))

# player salary api
@app.route('/api/player_birthplace')
def player_birthplace():
    return jsonify(list(player_birthplace_collection.find({ },
   { '_id': 0})))

    
app.run(debug=True, port=5000)
