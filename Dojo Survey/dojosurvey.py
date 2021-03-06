from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/results', methods=['POST'])
def usercreation():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    return render_template("result.html", name1 = name, location1 = location, language1 = language, comment1 = comment)

app.run(debug=True)