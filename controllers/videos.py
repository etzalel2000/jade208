from app import app
from flask import render_template, url_for, Flask, session, escape, request

@app.route('/videos')

def videos():

    return render_template("videos.html")
