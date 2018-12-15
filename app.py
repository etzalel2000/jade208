from flask import Flask
from flask import render_template

# Creates our Flask application.
app = Flask(__name__)

# Causes the website to rerender whenever you save your file
app.config["DEBUG"] = True
