import logging

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_cache import Cache

# Initialize logging
logging.basicConfig(level=logging.INFO,
                    format=' %(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)  # Initialize flask app
app.config.from_object('config')  # Initialize config from config.py
db = SQLAlchemy(app)  # Initialize database
CORS(app)  # Initialize non-CORS connection
bcrypt = Bcrypt(app)  # Initialize password hashing library
login_manager = LoginManager(app)  # Initialize login
cache = Cache(app, config={'CACHE_TYPE': 'simple'})  # Initialize caching system


# Models
from .models.user import *


# Views
from .views.login import *
from .views.company import *
from .views.regulator import *
from .views.customer import *
from .views.custodian import *
