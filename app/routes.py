from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Steve'}
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
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Store the request message for each user who is validated
        flash('Login requested for user {}, rememeber_me= {}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
