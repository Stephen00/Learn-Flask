from flask import Flask, render_template, flash, redirect, url_for
from forms import LoginForm

# Define project parameters
app = Flask(__name__)
app.config.from_pyfile('config.py')

# Index route
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Stevie'}
    posts = [
        {
            'author': {'username': 'Steve'},
            'body': 'How good was the new bond movie!',
        },
        {
            'author': {'username': 'Jennifer'},
            'body': 'I am currently learning flask!'
        },
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

# Login route
# Validates user login and redirects them to the homepage
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # store the request data internally and redirect the user
        flash('Login requested for user {}, remember me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


if __name__ == '__main__':
    app.run(debug=True)
