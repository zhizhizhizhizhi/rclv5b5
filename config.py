from os import environ 

SQLALCHEMY_DATABASE_URI = environ['DATABASE_URL'].replace('postgresql') 
SQLALCHEMY_TRACK_MODIFICATIONS = False