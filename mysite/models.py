'''
Database models. using sqlalchemy

Currently supporting the following models
Host - computers / servers on my network
User - Users of site
Book - books users have or are reading
'''


from mysite import db

class User(db.Model):
    '''
    User for tracking activity and use of site
    '''
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Book(db.Model):
    '''
    To track reading activity. Should be populated by goodreads data
    '''
    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(160), nullable=False)
    author = db.Column(db.String(120), nullable=False)
    series = db.Column(db.String(160))
    genre = db.Column(db.String(80))


class Post(db.Model):
    '''
    "blog" or note style data entered into site.
    '''
    post_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(160), nullable=False)
    content = db.Column(db.Text, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)


class Host(db.Model):
    '''
    Simple tracking of host for inventory etc
    '''
    host_id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(20))
    hostname = db.Column(db.String(120), nullable=False)

class Subnet(db.Model):
    '''
    Simple tracking of subnet ips
    '''
    ip = db.Column(db.String(20), primary_key=True)
    hostname = db.Column(db.String(120), nullable=True)
    last_updated = db.Column(db.DateTime, nullable=False)

class GitHubEvent(db.Model):
    '''
    to cache and track github events
    '''
    event_id = db.Column(db.Integer, primary_key=True)
    repo_id = db.Column(db.Integer, nullable=True)
#    event_timestamp = db.Column(db.DateTime, nullable=False)
    event_timestamp = db.Column(db.String(30), nullable=False)
    event_type = db.Column(db.String(20), nullable=False)

class Repo(db.Model):
    '''
    track source code repos. could be git or other?
    '''
    repo_id = db.Column(db.Integer, primary_key=True)
    repo_name = db.Column(db.String(32), nullable=False)
    repo_type = db.Column(db.String(20), nullable=False)
    repo_url = db.Column(db.String(120), nullable=True)

class Job(db.Model):
    '''
    for job processor
    '''
    job_id =  db.Column(db.Integer, primary_key=True)
    function = db.Column(db.String(160), nullable=False)
    status = db.Column(db.Integer, nullable=False, default=-1)
