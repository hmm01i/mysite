'''
View functions for app
'''
from flask import render_template, request, g
from mysite import app, db
from mysite.models import Host, Post

@app.route('/')
def index():
    '''
    root page
    '''
#    return('index')
    return render_template('index.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    '''
    admin functions for site

    init_database, etc
    '''
    msg = ''
    if request.method == 'POST':
        if request.form.get('submit') == 'init_db':
            db.create_all()
            msg = "DB initialized..."
    return render_template('admin.html', msg=msg)

@app.route('/activity')
def activity():
    '''
    meant to be like a news feed/activity stream
    '''
    return render_template('activity.html')

@app.route('/clients')
def clients():
    '''
    display clients on the network
    '''
    hosts = Host.query.all()
    return render_template('clients.html', clients=hosts)

@app.route('/blog')
def blog():
    '''
    users can view posts made to site. blog style
    '''
    # if user is logged in should also be able to create posts
    return render_template('blog.html')

@app.route('/create', methods=['GET', 'POST'])
def create():
    '''
    where users create posts
    '''
    if request.method == 'POST':
        if request.form.get('title') and request.form.get('content'):
            p = Post(title=request.form.get('title'), content=request.form.get('content'))
            db.session.add(p)
            db.session.commit()
            return render_template('entry.html')
        return render_template('error.html', error="failure posting")
    return render_template('create.html')
