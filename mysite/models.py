
from mysite import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(160), unique=True, nullable=False)
    author = db.Column(db.String(120), unique=True, nullable=False)
    series = db.Column(db.String(160), unique=True, nullable=False)
    genre = db.Column(db.String(80), unique=True, nullable=False)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(160), unique=True, nullable=False)
    content = db.Column(db.Text, unique=True, nullable=False)

