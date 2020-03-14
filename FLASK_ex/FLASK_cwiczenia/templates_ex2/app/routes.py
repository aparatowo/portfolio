from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Cervantes'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Heeellloooo Vietnam!'
        },
        {
            'author': {'username': 'Malkovich'},
            'body': 'I would like to C a movie...'
        },
        {
            'author': {'username': 'Travolta'},
            'body': 'It\'s saturday! Lets dance!'
        },
    ]

    return render_template('index.html', title='Home', user=user, posts=posts)