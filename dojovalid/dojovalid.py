from flask import Flask, render_template, request, redirect, flash, session
app = Flask(__name__)
app.secret_key = 'Secret'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/results', methods=['POST'])
def usercreation():
    if len(request.form['name']) < 1:
        flash("Name cannot be empty!") 
        # redundancy to check for both before redirect.
        if len(request.form['comment']) < 1 or len(request.form['comment']) > 250:
            flash("Comment section has no information or has more than 250 characters.")
        return redirect('/')
    if len(request.form['comment']) < 1 or len(request.form['comment']) > 250:
        flash("Comment section has no information or has more than 250 characters.")
        return redirect('/')
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    return render_template("result.html", name1 = name, location1 = location, language1 = language, comment1 = comment)

app.run(debug=True)