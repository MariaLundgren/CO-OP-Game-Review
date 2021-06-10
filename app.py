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
    # gets titles from db and sort them newest first
    titles = list(mongo.db.titles.find().sort("_id", -1))
    # get avg rating to title from reviews
    title_ratings = list(mongo.db.reviews.aggregate([
                {"$group": {
                    "_id": "$title_id",
                        "avg_rating": {"$avg": "$rating"}}}
                ]))
    return render_template("titles.html",
                           titles=titles,
                           title_ratings=title_ratings)


@app.route("/get_reviews")
def get_reviews():
    # gets reviews from db and sort them newest first
    reviews = list(mongo.db.reviews.find().sort("_id", -1))
    return render_template("selected_game_title.html", reviews=reviews)


@app.route("/search", methods=["GET", "POST"])
def search():
    # search based on game title
    query = request.form.get("query")
    titles = list(mongo.db.titles.find({"$text": {"$search": query}}))
    return render_template("titles.html", titles=titles)


@app.route("/add_game_title", methods=["GET", "POST"])
def add_game_title():
    # adds a game title to the db
    if "user" in session:
        if request.method == "POST":
            title = {
                "title_name": request.form.get("title_name"),
                "image_url": request.form.get("image_url"),
                "description": request.form.get("description"),
                "consoles": request.form.getlist("consoles"),
                "co_op_type": request.form.getlist("co_op_type"),
                "created_by": session["user"]
            }
            mongo.db.titles.insert_one(title)
            flash("Game title added.")
            # redirects user to titles template
            return redirect(url_for("get_titles"))
    else:
        return redirect(url_for("log_in"))
    return render_template("add_game_title.html")


@app.route("/selected_game_title/<title_id>")
def selected_game_title(title_id):
    # find selected title based on title_id
    title = mongo.db.titles.find_one({"_id": ObjectId(title_id)})
    # find reviews to selected title based on title_id
    reviews = mongo.db.reviews.find({"title_id": (title_id)})
    # gets avg title rating from reviews
    title_ratings = list(mongo.db.reviews.aggregate([
                {"$group": {
                    "_id": "$title_id",
                        "avg_rating": {"$avg": "$rating"}}}
                ]))
    return render_template("selected_game_title.html",
                           title=title, reviews=reviews,
                           title_ratings=title_ratings)


@app.route("/add_review/<title_id>", methods=["GET", "POST"])
def add_review(title_id):
    title = mongo.db.titles.find_one({"_id": ObjectId(title_id)})
    # adds a game review to the db
    if "user" in session:
        if request.method == "POST":
            review = {
                    "title_id": request.form.get("title_id"),
                    "review": request.form.get("review"),
                    "rating": int(request.form.get("rating")),
                    "created_by": session["user"]
                }
            mongo.db.reviews.insert_one(review)
            flash("Review added.")
        # redirects user to selected_game_title template
            return redirect(url_for("selected_game_title", title_id=title_id))
    else:
        return redirect(url_for("log_in"))
    return render_template("add_review.html", title=title)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # checks if user already exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exist. Please choose another username.")
            return redirect(url_for("register"))

        # adds user to db
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
        # chack if user exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # checks if password is correct
            if check_password_hash(
               existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))
            else:
                flash("Incorrect username and/or password")
                # redirects user back to log_in tempalte if password is wrong
                return redirect(url_for("log_in"))

        else:
            flash("Incorrect username and/or password")
            # redirects back to log_in template if username don't exist in db
            return redirect(url_for("log_in"))
    return render_template("log_in.html")


@app.route("/profile", methods=["GET", "POST"])
def profile():
    if "user" in session:
        # gets session user from db
        username = mongo.db.users.find_one(
            {"username": session["user"]})

        reviews = mongo.db.reviews.find().sort("_id", -1)
        # gets game titles added by user from db
        titles = mongo.db.titles.find().sort("_id", -1)
    else:
        return redirect("log_in")
    return render_template(
        "profile.html", username=username, reviews=reviews, titles=titles)


@app.route("/edit_profile", methods=["GET", "POST"])
def edit_profile():
    # updates users profile
    if "user" in session:
        username = mongo.db.users.find_one(
        {"username": session["user"]})
        if request.method == "POST":
            user_update = {"$set":
                {
                    "profile_image_url": request.form.get("profile_image_url"),
                    "favourite_game": request.form.get("favourite_game")
                }}
            mongo.db.users.update({"username": session["user"]}, user_update)
            flash("Profile Updated")

        mongo.db.users.find_one({"username": session["user"]})
    else:
        return redirect("log_in")
    return render_template("edit_profile.html", username=username)


@app.route("/edit_game_title/<title_id>", methods=["GET", "POST"])
def edit_game_title(title_id):
    # updates game title
    title = mongo.db.titles.find_one({"_id": ObjectId(title_id)})
    if "user" in session:
        if title['created_by'] == session["user"]:
            if request.method == "POST":
                submit = {
                    "title_name": request.form.get("title_name"),
                    "image_url": request.form.get("image_url"),
                    "description": request.form.get("description"),
                    "consoles": request.form.getlist("consoles"),
                    "co_op_type": request.form.getlist("co_op_type"),
                    "created_by": session["user"]
                }
                mongo.db.titles.update({"_id": ObjectId(title_id)}, submit)
                flash("Title Updated")
        else:
            return redirect(url_for("get_titles"))
    else:
        return redirect(url_for("log_in"))
    return render_template("edit_game_title.html", title=title)


@app.route("/delete_game_title/<title_id>")
def delete_game_title(title_id):
    # finds game title in db based on id
    title = mongo.db.titles.find_one({"_id": ObjectId(title_id)})
    if title['created_by'] == session["user"]:
        mongo.db.titles.remove({"_id": ObjectId(title_id)})
        # removes game title in db based on id
        mongo.db.reviews.remove({"title_id": (title_id)})
        flash("Title deleted")
    else:
        return redirect(url_for("get_titles"))
    return redirect(url_for("profile", username=session["user"]))


@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    # updates review
    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    if "user" in session:
        if review['created_by'] == session["user"]:
            if request.method == "POST":
                submit = {
                    "review": request.form.get("review"),
                    "rating": request.form.get("rating"),
                    "created_by": session["user"]
                }
                mongo.db.reviews.update({"_id": ObjectId(review_id)}, submit)
                flash("Review Updated")
        else:
            return redirect(url_for("get_titles"))
    else:
        return redirect(url_for("log_in"))
    return render_template("edit_review.html", review=review)


@app.route("/delete_review/<review_id>")
def delete_review(review_id):
    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    if review['created_by'] == session["user"]:
        # removes review in db based on id
        mongo.db.reviews.remove({"_id": ObjectId(review_id)})
        flash("Review deleted")
    else:
        return redirect(url_for("get_titles"))
    return redirect(url_for("profile", username=session["user"]))


@app.route("/log_out")
def log_out():
    # removes user from session coockie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("log_in"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
