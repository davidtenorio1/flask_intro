from flask import Flask
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/roll-dice')
def dice():
    roll = str(np.random.choice([1,2,3,4,5,6],3))
    roll = roll[1:-1]
    return ('You rolled ' + roll)