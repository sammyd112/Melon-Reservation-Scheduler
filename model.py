from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String) 

    def __repr__(self):
        return f'<User email={self.email}>'
    
class Reservation(db.Model):
    """A reservation."""

    __tablename__ = 'reservations'

    res_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    user_id = db.Column(db.Integer, 
                       db.ForeignKey('users.user_id'))
    res_datetime = db.Column(db.Datetime)
    

    def __repr__(self):
        return f'<User user_id={self.fname} ={self.email}>'

def connect_to_db(flask_app, db_uri="postgresql:///reservations", echo=False):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")

if __name__ == "__main__":
    from server import app
    with app.app_context():
        connect_to_db(app)