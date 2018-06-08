from flask import Flask, render_template, request
from mysite import app
from mysite.models import User

@app.route('/')
def index():
#    return('index')
    return render_template('index.html')


@app.route('/blog')
def blog():
    # if user is logged in should also be able to create posts
    return render_template('blog.html')

@app.route('/create', methods=['GET','POST'])
def create():
    if request.method == 'POST':
        if request.form.get('title') and request.form.get('content'):
            return render_template('entry.html')
        else:
            return render_template('error.html', error="failure posting")
    else:
        return render_template('create.html')
