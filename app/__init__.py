import os

from dotenv import load_dotenv
from flask import Flask, render_template

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
    return render_template('profile.html', title='Profile', url=os.getenv("URL"))

@app.errorhandler(404)
def page_not_found(e):
    source_img="./static/img/404.png"
    return render_template('404.html', img=source_img, title="Page not found"), 404
    

