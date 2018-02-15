from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")

@app.route('/process', methods=['POST'])
def usercreation():
    name = request.form['name']
    return render_template('process.html', name1 = name)

app.run(debug=True)