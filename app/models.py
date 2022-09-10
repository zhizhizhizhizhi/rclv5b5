from app import db
from datetime import datetime

class URL(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    original_url = db.Column(db.String, nullable=False)
    clicks = db.Column(db.Integer, nullable=False, default=0)