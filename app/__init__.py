import os

from dotenv import load_dotenv
from flask import Flask, render_template, json, current_app as app

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="Team Kenargi's portfolio", url=os.getenv("URL"))


@app.route('/project')
def get_project():
    project_file = os.path.join(app.static_folder, 'data', 'project.json')
    projects = []
    with open(project_file) as p:
        data = json.load(p)
        for i in data['projects']:
            projects.append(i)
    return render_template('project.html', projects=projects, url=os.getenv("URL"))


@app.route('/profile')
def get_profile():
    profile_file = os.path.join(app.static_folder, 'data', 'profile.json')
    profiles = []
    with open(profile_file) as p:
        data = json.load(p)
        for i in data['profiles']:
            profiles.append(i)
            print(profiles)
    return render_template('profile.html', profiles=profiles, title='Profile', url=os.getenv("URL"))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title='Page not found'), 404
