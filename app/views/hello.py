from flask import render_template

from app import app

@app.route('/hello/<name>', methods=['GET', 'POST'])
def hello(name=None):
    return render_template('hello.html', name=name)
