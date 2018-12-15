from app import app
from flask import render_template, url_for, Flask, session, escape, request

@app.route('/letter')

def letter():

    return render_template("letter.html")
