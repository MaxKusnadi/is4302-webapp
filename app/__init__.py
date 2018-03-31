import logging

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

logging.basicConfig(level=logging.INFO,
                    format=' %(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
CORS(app)

# Models
from app.models.user import *


@app.route("/")
def hello():
    return render_template('hello.html', message="Hello World!")
