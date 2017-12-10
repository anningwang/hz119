# -*- coding:utf-8 -*-
from flask import render_template, session
from app import app


@app.errorhandler(404)
def internal_error(error):
    print error
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    print error
    return render_template('500.html'), 500


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if 'username' in session:
        print session['username']
    return render_template('index.html', title='Home')


@app.route('/gj119', methods=['GET', 'POST'])
def gj119():
    return render_template('gj119.html', title='Home')


@app.route('/zd119', methods=['GET', 'POST'])
def zd119():
    return render_template('zd119.html', title='Home')


@app.route('/city119', methods=['GET', 'POST'])
def city119():
    return render_template('city119.html', title='Home')