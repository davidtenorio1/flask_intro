from flask import Flask
import numpy as np
import random
from flask import render_template, request
from model import predict

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/roll-dice<int:ndice>')
def rolldice(ndice):
    rolls = [random.randint(1, 6) for n in range(ndice)]
    output = '<h1>Here are your dice rolls:</h1>'
    output += '<br>'
    for roll in rolls:
        output += str(roll) + '<br>'
    print(output)
    return output

@app.route('/oregon_trail')
def trail():
    return 'You have died of dysentery!'

@app.route('/roll-dice')
def default():
    return 'Add the amount of dice you would like to roll to the end of the url'


@app.route('/my-first-form')
def my_first_form():
    return render_template('my-first-form.html')

@app.route('/make-greeting', methods=['POST'])
def handle_form_submission():
    name = request.form['name']
    title = request.form['title']

    greeting = 'Hello, '

    if title != '':
        greeting += title + ' '

    greeting += name + '!'

    return render_template('greeting-result.html', greeting=greeting)



@app.route("/predict-spam")
def show_spam_form():
    return render_template("predict-spam.html")


@app.route("/predict-spam-result", methods=["POST"])
def show_spam_result():
    message = request.form["message"]
    return render_template(
        "predict-spam-result.html", message=message, prediction=predict(message)
    )

