from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse


@app.route('/')
@app.route('/index')
@login_required
def index():
    posts = [
        {
            'author': {'username': 'Jamie'},
            'body': 'Love the new bond film!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'Currently learning Flask!'
        }
    ]
    return render_template('index.html', title='Home', posts=posts)


@app.route('/login', methods=['POST', 'GET'])
def login():
    # Check if the user is already logged in
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        # Query returns the user if it exists, or None if otherwise
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        # Otherwise successfully login the user
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        # prevents malicious exploitation of the next argument
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    # Add the user to the database if the form is validated
    if request.method == 'POST' and form.validate_on_submit():
        user = User(username=form.username.data, email=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You are now successfully registered!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)



