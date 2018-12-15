from app import app
from flask import render_template, url_for, Flask, session, escape, request

@app.route('/')

def home():

    return render_template("home.html")
