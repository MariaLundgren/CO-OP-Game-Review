'''
This file connects the website to the database.
'''
import os
from flask import (
    Flask, flash, render_template, redirect,
    request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
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
    '''
    Gets game titles from db and sort them newest first.
    Calculates the avg rating from reviews with the same title_id.
    Returns:
    Renders titles page.
    '''
    titles = list(mongo.db.titles.find().sort("_id", -1))
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
    '''
    Gets reviews from db and sort them newest first.
    Returns:
    Renders selected_game_title page.
    '''
    reviews = list(mongo.db.reviews.find().sort("_id", -1))
    return render_template("selected_game_title.html", reviews=reviews)


@app.route("/search", methods=["GET", "POST"])
def search():
    '''
    Searches game titles based on name of title.
    Returns:
    Renders the search results on titles page.
    '''
    query = request.form.get("query")
    titles = list(mongo.db.titles.find({"$text": {"$search": query}}))
    return render_template("titles.html", titles=titles)


@app.route("/add_game_title", methods=["GET", "POST"])
def add_game_title():
    '''
    Adds a new game title.
    Returns:
    If request is POST redirects the user to get_titles page.
    If request is GET renders add_game_title page.
    '''
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
            return redirect(url_for("get_titles"))
    else:
        return redirect(url_for("log_in"))
    return render_template("add_game_title.html")


@app.route("/selected_game_title/<title_id>")
def selected_game_title(title_id):
    '''
    Finds the selected game title and reviews with the same title_id.
    Calculates the avg rating from reviews with the same title_id.
    Args:
    title_id: id of a title and reviews with the same title_id.
    Returns:
    Renders selected_game_title page.
    '''
    title = mongo.db.titles.find_one({"_id": ObjectId(title_id)})
    reviews = mongo.db.reviews.find({"title_id": (title_id)})
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
    '''
    Adds a review for a given title.
    Args:
    title_id: id of a title to review.
    Returns:
    If request is POST redirects the user to selected_game_title page.
    If request is GET renders the add_review page.
    '''
    title = mongo.db.titles.find_one({"_id": ObjectId(title_id)})
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
            return redirect(url_for("selected_game_title", title_id=title_id))
    else:
        return redirect(url_for("log_in"))
    return render_template("add_review.html", title=title)


@app.route("/register", methods=["GET", "POST"])
def register():
    '''
    Adds a new users if the user don't already exists in db.
    Returns:
    Renders register page.
    '''
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exist. Please choose another username.")
            return redirect(url_for("register"))

        register_user = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email"),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register_user)

        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
        return redirect(url_for("profile"))
    return render_template("register.html")


@app.route("/log_in", methods=["GET", "POST"])
def log_in():
    '''
    Log in user if the user exist in db and
    the username and password is correct.
    Returns:
    If request is POST and username and password is correct,
    redirect user to profile page.
    If request is GET renders the log_in page.
    '''
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
               existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))

            flash("Incorrect username and/or password")
            return redirect(url_for("log_in"))
        flash("Incorrect username and/or password")
        return redirect(url_for("log_in"))
    return render_template("log_in.html")


@app.route("/profile", methods=["GET", "POST"])
def profile():
    '''
    Gets session user and the titles and reviews that
    that user have created, sorted newest first.
    Returns:
    Renders profile page.
    '''
    if "user" in session:
        username = mongo.db.users.find_one(
            {"username": session["user"]})

        reviews = mongo.db.reviews.find().sort("_id", -1)
        titles = mongo.db.titles.find().sort("_id", -1)
    else:
        return redirect("log_in")
    return render_template(
        "profile.html", username=username, reviews=reviews, titles=titles)


@app.route("/edit_profile", methods=["GET", "POST"])
def edit_profile():
    '''
    Gets session user and edits the user's profile.
    Returns:
    If request is POST redirects user to profile page.
    If request is GET renders the edit_profile page.
    '''
    if "user" in session:
        username = mongo.db.users.find_one(
            {"username": session["user"]})
        if request.method == "POST":
            user_update = {"$set":
                           {
                            "profile_image_url": request.form.get(
                                "profile_image_url"),
                            "favourite_game": request.form.get(
                                "favourite_game")
                           }}
            mongo.db.users.update({"username": session["user"]}, user_update)
            flash("Profile Updated")
            return redirect(url_for("profile"))

        mongo.db.users.find_one({"username": session["user"]})
    else:
        return redirect("log_in")
    return render_template("edit_profile.html", username=username)


@app.route("/edit_game_title/<title_id>", methods=["GET", "POST"])
def edit_game_title(title_id):
    '''
    Updates a game title.
    Args:
    title_id: id of a title.
    Returns:
    If request is POST redirects the user to profile page.
    If request is GET renders the edit_game_title page.
    '''
    title = mongo.db.titles.find_one({"_id": ObjectId(title_id)})
    if "user" in session:
        if title:
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
                    return redirect(url_for("profile"))
            else:
                flash(
                    "You don't have access to the page you tried to visit")
                return redirect(url_for("get_titles"))
        else:
            flash("The title you are trying to edit don't exist")
            return redirect(url_for("get_titles"))
    else:
        return redirect(url_for("log_in"))
    return render_template("edit_game_title.html", title=title)


@app.route("/delete_game_title/<title_id>")
def delete_game_title(title_id):
    '''
    Deletes a game title and all reviews to that title.
    Args:
    title_id: id of a title.
    Returns:
    Redirects user to profile page.
    '''
    title = mongo.db.titles.find_one({"_id": ObjectId(title_id)})
    if title['created_by'] == session["user"]:
        mongo.db.titles.remove({"_id": ObjectId(title_id)})
        mongo.db.reviews.remove({"title_id": (title_id)})
        flash("Title deleted")
    else:
        return redirect(url_for("get_titles"))
    return redirect(url_for("profile", username=session["user"]))


@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    '''
    Updates a review.
    Args:
    review_id: id of a review.
    Returns:
    If request is POST redirects the user to profile page.
    If request is GET renders the edit_review page.
    '''
    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    if "user" in session:
        if review:
            if review['created_by'] == session["user"]:
                if request.method == "POST":
                    review_update = {"$set":
                                     {
                                        "review": request.form.get("review"),
                                        "rating": int(request.form.get(
                                            "rating")),
                                        "created_by": session["user"]
                                     }}
                    mongo.db.reviews.update(
                        {"_id": ObjectId(review_id)}, review_update)
                    flash("Review Updated")
                    return redirect(url_for("profile"))
            else:
                flash(
                    "You don't have access to the page you tried to visit")
                return redirect(url_for("get_titles"))
        else:
            flash("The review you are trying to edit don't exist")
            return redirect(url_for("get_titles"))
    else:
        return redirect(url_for("log_in"))
    return render_template("edit_review.html", review=review)


@app.route("/delete_review/<review_id>")
def delete_review(review_id):
    '''
    Deletes a review.
    Args:
    review_id: id of a review.
    Returns:
    Redirects user to profile page.
    '''
    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    if review['created_by'] == session["user"]:
        mongo.db.reviews.remove({"_id": ObjectId(review_id)})
        flash("Review deleted")
    else:
        return redirect(url_for("get_titles"))
    return redirect(url_for("profile", username=session["user"]))


@app.route("/log_out")
def log_out():
    '''
    Removes user from session cookie.
    Returns:
    Redirects user to log_in page.
    '''
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("log_in"))


@app.errorhandler(404)
def page_not_found(error):
    '''
    Page not found error handler.
    Returns: Renders 404 page.
    '''
    return render_template("404.html", error=error)


@app.errorhandler(500)
def internal_server_error(error):
    '''
    Internal server error handler.
    Returns: Renders 500 page.
    '''
    return render_template("500.html", error=error)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
