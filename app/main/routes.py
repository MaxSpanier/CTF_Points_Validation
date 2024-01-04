from app.main import bp as main
from flask import redirect, current_app, render_template, flash

@main.route("/")
def index():
    flash("Flask app successfully loaded", "success")
    flash("Error while loading the Flask app", "error")
    return render_template("main.html")

# Test for pull requests and access
# TEST #2