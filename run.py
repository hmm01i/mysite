#!/usr/bin/env python
#from flask import Flask
from mysite import app

def create_tables():
    # Create table for each model if it does not exist.
    # Use the underlying peewee database object instead of the
    # flask-peewee database wrapper:
    db.create_all()

if __name__ == "__main__":
    create_tables
    app.run()
