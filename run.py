#!/usr/bin/env python
#from flask import Flask
from mysite import app, db
from mysite.database import create_tables

if __name__ == "__main__":
    create_tables()
    app.run(host='0.0.0.0')
