from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, Response, flash, redirect, url_for, jsonify, abort


                  
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


# VENUE MODEL
class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    image_link = db.Column(db.String(500))
    genres = db.Column(db.ARRAY(db.String))
    contact_id = db.Column(db.Integer, db.ForeignKey('ContactInfo.id'))  

# ARTIST MODEL
class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    genres = db.Column(db.ARRAY(db.String))
    image_link = db.Column(db.String(500))
    contact_id = db.Column(db.Integer, db.ForeignKey('ContactInfo.id'))

# SHOW MODEL
class Show(db.Model):
    __tablename__= 'Show'

    id = db.Column(db.Integer, primary_key = True)
    start_time = db.Column(db.DateTime)
    artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id'), nullable=False)

# CONTACT INFO FOR VENUE AND ARTIST MODEL
class ContactInfo(db.Model):
    __tablename__='ContactInfo'

    id = db.Column(db.Integer, primary_key = True)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    facebook_link = db.Column(db.String(120))

db.create_all()