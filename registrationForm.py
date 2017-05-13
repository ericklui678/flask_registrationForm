from flask import Flask, render_template, request, redirect, session, flash
import re
app = Flask(__name__)

app.secret_key = 'ThisIsSecret'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile('^[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    validCount = 0
    if len(request.form['firstName']) < 1:
        flash('First name is required', 'error')
    elif not NAME_REGEX.match(request.form['firstName']):
        flash('First name cannot contain numbers', 'error')
    else:
        validCount += 1

    if len(request.form['lastName']) < 1:
        flash('Last name is required', 'error')
    elif not NAME_REGEX.match(request.form['lastName']):
        flash('Last name cannot contain numbers', 'error')
    else:
        validCount += 1

    if len(request.form['email']) < 1:
        flash('Email is required', 'error')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Email is invalid', 'error')
    else:
        validCount += 1

    if len(request.form['password']) < 1:
        flash('Password is required', 'error')
    elif len(request.form['password']) <= 8:
        flash('Password needs to be more than 8 characters', 'error')
    else:
        validCount += 1

    if len(request.form['confirm']) < 1:
        flash('Password must be confirmed', 'error')
    elif (request.form['confirm'] != request.form['password']):
        flash('Passwords do not match', 'error')
    else:
        validCount += 1

    if validCount == 5:
        flash('You have submitted your information!', 'show')

    return redirect('/')

app.run(debug = True)

# elif not EMAIL_REGEX.match(request.form['email']):
