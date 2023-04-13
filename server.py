from flask import (Flask, redirect, request, render_template, session, jsonify, flash)
from datetime import datetime
from model import connect_to_db, db
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "secretsecretsecret"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    return render_template('base.html')



if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)