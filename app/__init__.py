import os

from dotenv import load_dotenv
from flask import Flask, render_template

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))


@app.route('/profile')
def get_profile():
    return render_template('profile.html', title='Profile', url=os.getenv("URL") + "/profile")
