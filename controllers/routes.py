from flask import Blueprint, render_template

# Make Blueprints
index = Blueprint("index", __name__, url_prefix="/")
about = Blueprint("about", __name__, url_prefix="/about-me")
projects = Blueprint("projects", __name__, url_prefix="/projects")
contact = Blueprint("contact", __name__, url_prefix="/contact-me")

# Primary route and initial page.
@index.route("/", methods=["GET"])
def index_page():
    return render_template('index.html')

# About me page route
@about.route("/", methods=["GET"])
def about_page():
    return render_template('about.html')

# Projects page for more credibility
@projects.route("/", methods=["GET"])
def projects_page():
    return render_template('projects.html')

# Contact page for send emails and talk with me on whatssapp
@contact.route("/", methods=["GET", "POST"])
def contact_page():
    return render_template('contact.html')


