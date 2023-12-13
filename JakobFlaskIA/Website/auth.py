from flask import Blueprint, render_template, request, flash, redirect, url_for
from .model import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))



@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get['email']
        username = request.form.get['username']
        password = request.form.get['password']
        password_confirm = request.form.get['password-confirm']

        if len(email) < 4:
            flash("email must be at least 4 characters long", category='error')
            pass
        elif len(username) < 2:
            flash("Username must be at least 2 characters long", category='error')
            pass
        elif password != password_confirm:
            flash("Passwords do not match", category='error')
            pass
        elif len(password) < 8:
            flash("Password must be at least 8 characters long", category='error')
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(
                password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

        return render_template("sign_up.html", user=current_user)
            # add user to database
    return render_template("signup.html")