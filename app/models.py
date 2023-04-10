# Add any model classes for Flask-SQLAlchemy here
from . import db

class Movie(db.Model):

    __tablename__='movies'

    id = db.Column(db.Integer, primary_key=True)
    title= db.Column(db.string(255))
    description= db.Column(db.text(255))
    poster= db.Column(db.string(255))
    created_at= db.Column(db.timestamp)

    def __init__(self,title,description,poster,created_at):
        self.title = title
        self.description = description
        self.poster = poster
        self.created_at = created_at

