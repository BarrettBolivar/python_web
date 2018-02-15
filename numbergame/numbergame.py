from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

def setSession():
    num1 = random.randrange(0, 101)
    session['num'] = num1

@app.route('/')
def index():
    if session['num'] == None:
        setSession()
    else:
        pass
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def checkNumber():
    fail = 0
    success = 0
    guess = request.form['guess']
    intguess = int(guess)
    if intguess == session['num']:
        success = 1
    elif intguess > session['num']:
        fail = 1
    elif intguess < session['num']:
        fail = 2
    return render_template('index.html', success = success, fail = fail)

@app.route('/reset', methods=['POST'])
def reset():
    setSession()
    return redirect('/')

app.run(debug=True)