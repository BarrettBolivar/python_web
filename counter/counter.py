from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'Secret'

@app.route('/')
def index():
    session['counter'] += 1
    return render_template('index.html', counter=session['counter'])

@app.route('/increment', methods=['POST'])
def increment_by_two():
    session['counter'] += 1
    return redirect('/')

@app.route('/clear', methods=['POST'])
def clear():
    session['counter'] = 0
    return redirect('/')

app.run(debug=True)