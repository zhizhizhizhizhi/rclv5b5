from os import environ 

SQLALCHEMY_DATABASE_URI = environ['DATABASE_URL'].replace('postgres', 'postgresql') 
SQLALCHEMY_TRACK_MODIFICATIONS = False