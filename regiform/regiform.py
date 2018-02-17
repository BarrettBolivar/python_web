from flask import Flask, render_template, request, redirect, flash, session
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'Secret'


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/results', methods=['POST'])
def usercreation():
    fnamestr = str(request.form['fname'])
    lnamestr = str(request.form['lname'])
    if len(request.form['email']) < 1:
        flash("") 
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
    elif len(request.form['fname']) < 1:
        flash("first name form empty")
    elif len(request.form['lname']) < 1:
        flash("last name form empty")
    elif not str.isalpha(fnamestr) or not str.isalpha(lnamestr):
        flash("Names cannot contain any numbers")
    elif len(request.form['password']) < 8:
        flash("password contains less than 8 characters")
    elif request.form['password'] != request.form['cpassword']:
        flash("passwords do not match")
    else:
        flash('Success')
    return redirect('/')

app.run(debug=True)
