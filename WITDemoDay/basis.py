#!/usr/bin/env python3

from flask import (Flask,render_template,request,flash,url_for,session)

# import models 

app = Flask(__name__)


# app.config["SECRET_KEY"] = open("SECRET_KEY", "rb").read()

# Frontpage
@app.route('/')
def home():
    return render_template('index.html')

# Register
@app.route('/check-credentials-register', methods=["POST"])
def check_credentials_register():
    __email = request.form['email']
    __password = request.form['password']
#   We are skipping at least two important cybersec. practices:
#       1) We're not hashing the inputs
#       2) We're not evaluating against None or null
#       3) We're not checking a database-- this is hard coded
    result = models.User.register(__email, __password)
    if result == False:
        flash('that email already exists, please use it to login.')
        return home()
    else:
        return profile_setup()

@app.route('/profile_setup', methods=["POST"])
def profile_setup():
    email=session['email']
    user_id = modesl.User.get_id(email)
    models.User.update_profile(__name, __title, __industry, __interests, __description, __looking_for, __organizations, __education, __links)
    return profile()

@app.route('/profile')
def profile():
    return render_template('profile.html')


# @app.route('/tweet', methods=["POST"])
# def tweet():
#     __tweet = request.form['twttr'] # from html form name, __tweet is a string from user form
#     # print(__tweet)
#     username = session['username']
#     user_id = models.User.get_id(username)
#     models.Tweet.store_tweet(__tweet, user_id)
#     return dashboard()


# Login
@app.route('/check-credentials-login', methods=["POST"])
def check_credentials_login():
    __email = request.form['email']
    __password = request.form['password']
#   We are skipping at least two important cybersec. practices:
#       1) We're not hashing the inputs
#       2) We're not evaluating against None or null
#       3) We're not checking a database-- this is hard codedresult = models.User.register(__username, __password)
    result = models.User.login(__email, __password)
    if result == False:
        flash('incorrect login, try again')
        return serve_login()
    else:
        session['email']=__email
        matches=models.Match.priv(__email)
        return dashboard()
        # render_template('dashboard.html', user_tweets=tweets, username=__username)

# Dashboard - unconscious bias edu
@app.route('/dashboard')
def dashboard():
    return render_template('questions.html')

@app.route('/tutorial')
def tutorial():
    return render_template('tutorial.html')

    # def dashboard():
    #     username=session['username']
    #     tweets=models.Tweet.priv(username)
    #     return render_template('dashboard.html', username=username, user_tweets=tweets)




# Matches
@app.route('/matches')
def matches():
    username=session['username']
    matches=models.Match.priv(username)
    return render_template('dashboard.html', username=username, user_matches=matches)





# @app.route('/tweet', methods=["POST"])
# def tweet():
#     __tweet = request.form['twttr'] # from html form name, __tweet is a string from user form
#     # print(__tweet)
#     username = session['username']
#     user_id = models.User.get_id(username)
#     models.Tweet.store_tweet(__tweet, user_id)
#     return dashboard()



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5002, debug=True)