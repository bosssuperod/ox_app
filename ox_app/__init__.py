# Import the framework
from flask import Flask, flash, request, render_template, redirect, url_for

from flask_mysqldb import MySQL

import os, json
from dotenv import load_dotenv


# env var
load_dotenv()

app = Flask(__name__)

mysql = MySQL(app)


# configure
app.config['MYSQL_HOST'] = os.environ['MYSQL_HOST']
app.config['MYSQL_USER'] = os.environ['MYSQL_USER']
app.config['MYSQL_PASSWORD'] = os.environ['MYSQL_PASSWORD']
app.config['MYSQL_DB'] = os.environ['MYSQL_DB']


# Default home view
@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

# List all players
@app.route('/getplayers', methods=['GET'])
def all_players():
    db =  mysql.connection.cursor()
    db.execute('''select id, name, victory, defeat, draw, is_play, game_id  from players;''')
    row_headers=[x[0] for x in db.description] #this will extract row headers
    rv = db.fetchall()
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))
    return json.dumps(json_data)

# Add new player
@app.route('/players', methods=['GET','POST'])
def add_player():
    if request.method == 'POST':
        name = request.form['name']
        db =  mysql.connection.cursor()
        db.execute("INSERT INTO players (name) VALUES (%s)", (name,))
        mysql.connection.commit()
        db.close()
        return redirect(url_for('index'))

    return render_template('addPlayer.html')

@app.route('/game', methods=['GET'])
def game():
    return render_template('board.html')

