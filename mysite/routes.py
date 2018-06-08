from flask import Flask, render_template
from mysite import app
from mysite.models import User

@app.route('/')
def index():
#    return('index')
    return render_template('index.html')


@app.route('/blog/')
def blog():
    # if user is logged in should also be able to create posts
    return render_template('blog.html')
