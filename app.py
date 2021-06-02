import os
from flask import (
    Flask, flash, render_template, redirect,
    request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
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


@app.route("/get_reviews")
def get_reviews():
    reviews = list(mongo.db.reviews.find())
    return render_template("selected_game_title.html", reviews=reviews)


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


@app.route("/selected_game_title/<title_id>")
def selected_game_title(title_id):
    title = mongo.db.titles.find_one({"_id": ObjectId(title_id)})
    reviews = mongo.db.reviews.find({"title_id": (title_id)})
    return render_template(
        "selected_game_title.html", title=title, reviews=reviews)


@app.route("/add_review/<title_id>", methods=["GET", "POST"])
def add_review(title_id):
    title = mongo.db.titles.find_one({"_id": ObjectId(title_id)})
    if request.method == "POST":
        review = {
                "title_id": request.form.get("title_id"),
                "review": request.form.get("review"),
                "rating": request.form.get("rating")
            }
        mongo.db.reviews.insert_one(review)
    return render_template("add_review.html", title=title)


@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
