from flask import Flask, render_template, request, redirect, session, flash
import re
import datetime
app = Flask(__name__)

app.secret_key = 'ThisIsSecret'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile('^[a-zA-Z]+$')
PW_REGEX = re.compile('^(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]')

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
    elif not PW_REGEX.match(request.form['password']):
        flash('Password needs at least 1 uppercase and 1 digit', 'error')
    else:
        validCount += 1

    if len(request.form['confirm']) < 1:
        flash('Password must be confirmed', 'error')
    elif (request.form['confirm'] != request.form['password']):
        flash('Passwords do not match', 'error')
    else:
        validCount += 1

    current = str(datetime.datetime.now().strftime('%Y-%m-%d'))
    cYear = int(current[:4])
    cMonth = int(current[5:7])
    cDay = int(current[8:])

    bday = str(request.form['date'])
    bYear = int(bday[:4])
    bMonth = int(bday[5:7])
    bDay = int(bday[8:])

    if len(request.form['date']) < 1:
        flash('Birthday is required')
    elif len(request.form['date']) > 10:
        print len(request.form['date'])
        flash('Birthday is invalid')
    elif (bYear > cYear) or (bYear == cYear and bMonth > cMonth) or (bYear == cYear and bMonth == cMonth and bDay > cDay):
        flash('Birthday must be in the past')
    else:
        validCount += 1

    if validCount == 5:
        flash('You have submitted your information!', 'show')

    return redirect('/')

app.run(debug = True)
