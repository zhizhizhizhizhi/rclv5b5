import config

from flask import Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SECRET_KEY'] = 'SECRET_KEY'

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

from app import models
from flask_migrate import Migrate
migrate = Migrate(app,db)

from hashids import Hashids
import random, string
hashids = Hashids(min_length=4, salt=''.join(random.choice(string.printable) for i in range(6)))

from app import routes

