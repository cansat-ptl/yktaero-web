import os, sys
from flask import Flask

version_string = "v0.0.1-dev"

basedir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.dirname(basedir))

from config import CurrentConfig

app = Flask(__name__)
app.config.from_object(CurrentConfig)

from app import pages