from flask import Flask, render_template, request
from mysite import app, db
from mysite.models import User, Post

@app.route('/')
def index():
#    return('index')
    return render_template('index.html')

@app.route('/admin', methods=['GET','POST'])
def admin():
    msg = ''
    if request.method == 'POST':
        if request.form.get('submit') == 'init_db':
            db.create_all()
            msg = "DB initialized..."
    return render_template('admin.html',msg=msg)

@app.route('/activity')
def activity():
    return render_template('activity.html')

@app.route('/blog')
def blog():
    # if user is logged in should also be able to create posts
    return render_template('blog.html')

@app.route('/create', methods=['GET','POST'])
def create():
    if request.method == 'POST':
        if request.form.get('title') and request.form.get('content'):
            p = Post(title=request.form.get('title'), content=request.form.get('content'))
            db.session.add(p)
            db.session.commit()
            return render_template('entry.html')
        else:
            return render_template('error.html', error="failure posting")
    else:
        return render_template('create.html')
