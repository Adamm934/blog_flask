
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def display_things():
    return render_template('home.html')