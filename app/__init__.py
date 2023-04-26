from flask import Flask, render_template, abort

# could alternatively store in some DB...
projects = [
    {
        "name": "Securities master database",
        "thumb": "img/securities-master-database.png",
        "hero": "img/securities-master-database.png",
        "categories": ["Python", "SQL"],
        "slug": "securities-master-database",
        # "prod": "https://udemy.com",
    },
    {
        "name": "Equity factor risk decomposition",
        "thumb": "img/factor-risk.png",
        "hero": "img/factor-risk.png",
        "categories": ["Python", "PowerBI", "SQL"],
        "slug": "factor-risk",
    },
    {
        "name": "Predicting equity share prices using LSTM models",
        "thumb": "img/lstm-equity-prediction.png",
        "hero": "img/lstm-equity-prediction.png",
        "categories": ["Python", "Machine Learning"],
        "slug": "lstm-equity-prediction",
    },
]

slug_to_project = {project["slug"]: project for project in projects}

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html", projects=projects)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/project/<string:slug>")
def project(slug):
    if slug not in slug_to_project:
        abort(404)
    return render_template(f"project_{slug}.html", project=slug_to_project[slug])


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404
