from flask import Flask
from flask import render_template

# Establish connection to local host 27017
conn = 'mongodb://localhost:27017'

# Connect to MongoClient
client = pymongo.MongoClient(conn)


app = Flask(__name__)

@app.route('/index')
def about():
    return render_template("index.html")

@app.route('/about)
def about():
    return render_template("about.html")

# app route for api
@app.route("/api/v1.0/nba_player_info")
def players():
    """Return player data as json"""
    # Create session link for Python to DB
    query = db.testing_beds.find_one()

    # Use a for loop to confirm data is now located in the database
    all_players = []
    for player in query:
        all_players.append(player)

    return jsonify(all_results)
    
app.run(debug=True, port=5000)
