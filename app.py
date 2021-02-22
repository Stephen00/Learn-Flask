from flask import Flask, render_template

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(debug=True)
