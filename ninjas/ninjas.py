from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/', defaults={'path': ''})
def index():
    return render_template("index.html")

@app.route('/ninja')
def ninjas():
    return render_template("ninja.html")

@app.route('/ninja/blue')
def ninjablue():
    return render_template("ninjablue.html")

@app.route('/ninja/red')
def ninjared():
    return render_template("ninjared.html")

@app.route('/ninja/orange')
def ninjaorange():
    return render_template("ninjaorange.html")

@app.route('/ninja/purple')
def ninjapurple():
    return render_template("ninjapurple.html")

@app.route('/<path:path>')
def catch_all(path):
    return render_template("notaapril.html")

app.run(debug=True)
