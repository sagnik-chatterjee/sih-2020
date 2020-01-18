import flask
from flask import request, jsonify
import pandas as pd
import json
import os
import random
import string

app = flask.Flask(__name__)
app.config["DEBUG"] = True

df=pd.read_csv('sih_final.csv')
data=df.to_dict('records')

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route('/', methods=['GET'])
def home():
    return '''<h1> SIH Sentiment Analysis </h1>
<p>A Prototype API that can convert CSV to JSON</p>'''

def generate_key(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))


@app.route('/api/v1/resources/data/all', methods=['GET'])
def api_all():
    key=generate_key(10)
    return jsonify(data)

app.run()

