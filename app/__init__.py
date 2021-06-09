import os

from dotenv import load_dotenv
from flask import Flask, render_template

load_dotenv()
app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html', title="TEAM: KENARGI", url=os.getenv("URL"))

@app.route('/project')
def project():
    projects = [
        {
            'name': 'projectone',
            'description': 'Beautiful day in Portland!',
            'tools': 'React',
            'link': 'www.google.com',
            'source': 'www.github.com'
        },
        {
            'name': 'projecttwo',
            'description': 'Beautiful day in Georgia!',
            'tools': 'Python',
            'link': 'www.github.com',
            'source': 'www.google.com'
        }
    ]

    return render_template('project.html', projects=projects, url=os.getenv("URL"))


@app.route('/profile')
def get_profile():
    return render_template('profile.html', title='Profile', url=os.getenv("URL") + "/profile")
