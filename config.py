import os

SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or \
    'postgresql://localhost/url-shortener'
SQLALCHEMY_TRACK_MODIFICATIONS = False