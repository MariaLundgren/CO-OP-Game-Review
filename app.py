import os
from flask import (
    Flask, flash, render_template, redirect,
    request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_titles")
def get_titles():
    titles = list(mongo.db.titles.find())
    return render_template("titles.html", titles=titles)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    titles = list(mongo.db.titles.find({"$text": {"$search": query}}))
    return render_template("titles.html", titles=titles)


@app.route("/add_game_title", methods=["GET", "POST"])
def add_game_title():
    if request.method == "POST":
        title = {
            "title_name": request.form.get("title_name"),
            "image_url": request.form.get("image_url"),
            "description": request.form.get("description"),
            "consoles": request.form.getlist("consoles"),
            "local_or_online": request.form.getlist("local_or_online")
        }
        mongo.db.titles.insert_one(title)
    return render_template("add_game_title.html")


@app.route("/selected_game_title")
def selected_game_title():
    return render_template("selected_game_title.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
