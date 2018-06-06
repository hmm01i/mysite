from flask import Flask, render_template
from mysite import app
from mysite.models import User

@app.route('/')
def index():
#    return('index')
    return render_template('index.html')

