from __future__ import with_statement
from flask import Flask
from flask.globals import _app_ctx_stack, request
from flask.helpers import flash, url_for
from flask.templating import render_template
from sqlite3 import dbapi2
from werkzeug.utils import redirect

# configuration
DATABASE = 'blog.db'
DEBUG = True

SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'admin'
KEEP='keep'

app = Flask(__name__)
config = app.config.from_object(__name__)

def get_db():
    top = _app_ctx_stack.top
    if not hasattr(top, "sqlite_db"):
        top.sqlite_db = dbapi2.connect(app.config['DATABASE'])
    return top.sqlite_db
        

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource("schema.sql") as f:
            db.cursor().executescript(f.read())
        db.commit()
        
@app.route('/')
def show_entries():
    db = get_db()
    cur = db.execute('select title, text from entries order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=["post"])
def add_entry():
    db = get_db()
    db.execute('insert into entries (title, text) values (?, ?)', [request.form['title'], request.form['text']])
    db.commit()
    flash('new entry has been posted successfully')
    return redirect(url_for('show_entries'))
    
if __name__ == '__main__':
# init_db()
    app.run()
            
