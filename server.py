from flask import (Flask, redirect, request, render_template, session, jsonify, flash)
from datetime import datetime
from model import connect_to_db, db
from jinja2 import StrictUndefined
import crud

app = Flask(__name__)
app.secret_key = "secretsecretsecret"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def display_homepage():
    return render_template("homepage.html")

@app.route('/email', methods = ['POST'])
def login():
    email = request.form['user-email']
    print(email)
    user = crud.get_user_by_email(email)
    if user == None:
        user = crud.create_user(email)
        db.session.add(user)
        db.session.commit()
        session["user_email"] = user.email
    else:
        session["user_email"] = user.email
    return render_template("homepage.html")

@app.route('/showtimes', methods=["POST"])
def show_times():
    date = request.json['date']
    avaliable_times = crud.create_avaliable_times_dict(date)
    taken_times = crud.get_all_reservations_times(date)
    return avaliable_times

@app.route('/newres', methods = ['POST'])
def add_reservation():
    # date = request.json['date']
    email = session['user_email']
    user = crud.get_user_by_email(email)
    time = request.json['time']
    time = time + ":00"
    print(time)
    date = request.json['date']
    new_reservation = crud.create_reservation(user.user_id, date, time)
    db.session.add(new_reservation)
    db.session.commit()
    print('success')
    return render_template('homepage.html')

@app.route('/seeres')
def show_reservations():
    email = session['user_email']
    user = crud.get_user_by_email(email)
    reservations = crud.get_reservations(user.user_id)
    return reservations

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)