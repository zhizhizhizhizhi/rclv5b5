import os

SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or \
    'postgres://lqqiacheenotxq:1a9ff45fbb6030b7d9f431f281fc659a1d9f8a94f80a21ae79bcdf230c7220e4@ec2-34-200-205-45.compute-1.amazonaws.com:5432/dbm4asj0lps98v'
    # 'postgresql://localhost/url_shortener'
SQLALCHEMY_TRACK_MODIFICATIONS = False