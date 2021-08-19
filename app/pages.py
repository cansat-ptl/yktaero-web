import os, sys

basedir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.dirname(basedir))

from flask import request, jsonify, render_template, url_for, redirect
from app import app

def str2bool(v):
    return v.lower() in ("yes", "true", "t", "1")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/news')
def news():
    return render_template('news.html')
