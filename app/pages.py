import os, sys
from flask import send_from_directory

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

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/about/staff')
def staff():
    return render_template('about/staff.html')

@app.route('/about/partners')
def partners():
    return render_template('about/partners.html')

@app.route('/projects/payloads')
def payloads():
    return render_template('projects/payloads.html')

@app.route('/projects/yktsat')
def yktsat():
    return render_template('projects/yktsat.html')

@app.route('/projects/sounding-rockets')
def rockets():
    return render_template('projects/sounding-rockets.html')

@app.route('/projects/ground-equipment')
def ground():
    return render_template('projects/ground-equipment.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')