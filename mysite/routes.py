from flask import Flask, render_template
from mysite import app, config, database

@app.route('/')
def index():
#    return('index')
    return render_template('index.html')
