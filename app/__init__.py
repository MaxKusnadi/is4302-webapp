import logging

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_cache import Cache


logging.basicConfig(level=logging.INFO,
                    format=' %(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
CORS(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})


# Models
from .models.user import *


# Views
from .views.login import *
from .views.company import *
<<<<<<< HEAD
from .views.customer import *
=======
from .views.regulator import *
>>>>>>> 9886312a19d96d85fe6fe9121831ec38f0d525d0
