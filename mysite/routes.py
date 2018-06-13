'''
View functions for app
'''
import datetime
from flask import render_template, request, redirect, url_for, g
from mysite import app, db
from mysite.models import Host, Post, Subnet

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
            db.drop_all()
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
    hosts = Subnet.query.all()
    return render_template('clients.html', clients=hosts)

@app.route('/blog')
def blog():
    '''
    users can view posts made to site. blog style
    '''
    # if user is logged in should also be able to create posts
    posts = Post.query.all()
    return render_template('blog.html', posts=posts)

@app.route('/create', methods=['GET', 'POST'])
def create():
    '''
    where users create posts
    '''
    if request.method == 'POST':
        if request.form.get('title') and request.form.get('content'):
            post = Post(title=request.form.get('title'),
                        content=request.form.get('content'),
                        create_date=datetime.datetime.now())
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('entry', post_id=post.post_id))
#            return render_template('entry.html', post=)
        return render_template('error.html', error="failure posting")
    return render_template('create.html')

@app.route('/enties/<int:post_id>')
def entry(post_id):
    '''
    display a single entry
    '''
    post = Post.query.filter_by(post_id=post_id).first()
    return render_template('entry.html', post=post)
