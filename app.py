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
            "local_or_online": request.form.getlist("local_or_online"),
            "created_by": session["user"]
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
                "rating": request.form.get("rating"),
                "created_by": session["user"]
            }
        mongo.db.reviews.insert_one(review)
    return render_template("add_review.html", title=title)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exist. Please choose another username.")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email"),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
    return render_template("register.html")


@app.route("/log_in", methods=["GET", "POST"])
def log_in():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
               existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))
            else:
                flash("Incorrect username and/or password")
                return redirect(url_for("log_in"))

        else:
            flash("Incorrect username and/or password")
            return redirect(url_for("log_in"))
    return render_template("log_in.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    reviews = mongo.db.reviews.find()
    titles = mongo.db.titles.find()
    return render_template(
        "profile.html", username=username, reviews=reviews, titles=titles)


@app.route("/edit_profile/<user_id>", methods=["GET", "POST"])
def edit_profile(user_id):
    if request.method == "POST":
        submit = {
                "user": request.form.get("user"),
                "profile_image_url": request.form.get("profile_image_url"),
                "favourite_game": request.form.get("favourite_game")
        }
        mongo.db.users.update({"_id": ObjectId["user_id"]}, submit)
        flash("Profile Updated")

    user = mongo.db.users.find_one({"_id": ObjectId["user_id"]})
    return render_template("edit_profile.html", user=user)


@app.route("/edit_game_title/<title_id>", methods=["GET", "POST"])
def edit_game_title(title_id):
    if request.method == "POST":
        submit = {
            "title_name": request.form.get("title_name"),
            "image_url": request.form.get("image_url"),
            "description": request.form.get("description"),
            "consoles": request.form.getlist("consoles"),
            "local_or_online": request.form.getlist("local_or_online"),
            "created_by": session["user"]
        }
        mongo.db.titles.update({"_id": ObjectId(title_id)}, submit)
        flash("Title Updated")

    title = mongo.db.titles.find_one({"_id": ObjectId(title_id)})
    return render_template("edit_game_title.html", title=title)


@app.route("/delete_game_title/<title_id>")
def delete_game_title(title_id):
    mongo.db.titles.remove({"_id": ObjectId(title_id)})
    mongo.db.reviews.remove({"title_id": (title_id)})
    flash("Title deleted")
    return redirect(url_for("profile", username=session["user"]))


@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    if request.method == "POST":
        submit = {
            "review": request.form.get("review"),
            "rating": request.form.get("rating"),
            "created_by": session["user"]
        }
        mongo.db.reviews.update({"_id": ObjectId(review_id)}, submit)
        flash("Review Updated")

    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    return render_template("edit_review.html", review=review)


@app.route("/delete_review/<review_id>")
def delete_review(review_id):
    mongo.db.reviews.remove({"_id": ObjectId(review_id)})
    flash("Review deleted")
    return redirect(url_for("profile", username=session["user"]))


@app.route("/log_out")
def log_out():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("log_in"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
