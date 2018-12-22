from app import app
from flask import render_template, url_for, Flask, session, escape, request

@app.route('/semester1')

def semester1():

    return render_template("semester1.html")
