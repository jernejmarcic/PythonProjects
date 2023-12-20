# Will show routes, like URLs to find and stuff
from flask import Blueprint, render_template

auth = Blueprint('auth', __name__) #Can change name but for better if its same

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up',methods=['GET', 'POST'])
def sign_up():
    return render_template("signup.html")