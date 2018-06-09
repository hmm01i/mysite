'''
Flask app intialization
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('mysite.config')

db = SQLAlchemy(app)

import mysite.routes
