from app import app
from flask import render_template, url_for, Flask, session, escape, request

@app.route('/pics')

def pics():

    return render_template("pics.html")
