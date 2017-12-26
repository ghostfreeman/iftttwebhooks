"""
Coffee.py

Runs the commands needed when my Google Home routine fires to make
a nice pot of Coffee
"""

from flask import Flask, request
from pyfttt import *
import json

# This is the POST action that basically fires off the WeMo to turn on

app = Flask(__name__)

@app.route("/startcoffee", method=["POST"])
def brew():
    
