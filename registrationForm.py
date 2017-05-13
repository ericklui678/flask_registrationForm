from flask import Flask, render_template, request, redirect, session, flash
import re
app = Flask(__name__)

app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    print 'Got Post Info'
    if len(request.form['firstName']) < 1:
        flash('First name is required')
    if len(request.form['lastName']) < 1:
        flash('Last name is required')
    if len(request.form['email']) < 1:
        flash('Email is required')
    if len(request.form['password']) < 1:
        flash('Password is required')
    if len(request.form['confirm']) < 1:
        flash('Password needs to be confirmed')
    return redirect('/')

app.run(debug = True)
