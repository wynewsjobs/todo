'''
Created on Oct 16, 2012

@author: Lucas
'''
from flask import render_template, jsonify, Flask, request

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/add_num')
def add_number():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result = a+b)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
# init_db()
    app.run()