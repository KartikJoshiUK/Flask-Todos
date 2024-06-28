from flask import Blueprint, render_template

templatesRouter = Blueprint("/templates", __name__)

@templatesRouter.route("/")
def index():
    return render_template("index.html")

@templatesRouter.route("/about")
def about():
    return render_template("about.html")

@templatesRouter.route("/dynamic/<string:name>")
def dynamic(name):
    print(name)
    return render_template("dynamic.html", name=name)