import os

from dotenv import load_dotenv
from flask import Flask, render_template, json, current_app as app
from helper import read_file
load_dotenv()
app = Flask(__name__)




@app.route('/')
@app.route('/index')
def index():

    img_1 = './static/img/friends.jpg'
    img_2 = "./static/img/Gigi_Hui.png"
    img_3 = "./static/img/friends.jpg"
    return render_template('index.html', title="Team Kenargi's portfolio", url=os.getenv("URL"),
    img_1=img_1, img_2=img_2, img_3=img_3)



@app.route('/project')
def get_project():
    project_file = os.path.join(app.static_folder, 'data', 'project.json')
    projects = read_file(project_file)  
    return render_template('project.html', projects=projects, url=os.getenv("URL"))


@app.route('/profile')
def get_profile():
    profile_file = os.path.join(app.static_folder, 'data', 'profile.json')
    profiles = read_file(profile_file)
    return render_template('profile.html', profiles=profiles, title='Profile', url=os.getenv("URL"))

  
@app.errorhandler(404)
def page_not_found(e):
    source_img="./static/img/404.png"
    return render_template('404.html', img=source_img, title="Page not found"), 404
    

