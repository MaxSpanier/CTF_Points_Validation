from flask import render_template, flash, redirect, url_for
from app import app, login_manager
from app.forms import FlagForm, LoginForm
from app.models import User

from flask_login import login_user, logout_user, login_required, current_user

import hashlib, bcrypt, boto3

# DynamoDB setup
dynamodb = boto3.resource("dynamodb")
# test-user -- 1q2w3e4r5t

@app.route("/")
def index():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))
    else:
        return redirect(url_for("login"))

# ------------------------------ Flag Verification --------------------------- #

@login_required
@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    form = FlagForm()
    if form.validate_on_submit():
        return render_template("main.html", title="CLOUDYRION CTF 2024", form=form)
    return render_template("main.html", title="CLOUDYRION CTF 2024", form=form)

# ------------------------------ Login / Logout ------------------------------ #

@login_manager.user_loader
def load_user(user_id):
    # Fetch user from DynamoDB
    table = dynamodb.Table("CareerDay_UserData")
    response = table.get_item(
        Key = {
            "username": user_id
        })
    user = response.get("Item")
    if user:
        return User(user_id)
    return None

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = get_user_data(username)
        if user and hashlib.md5(password.encode("UTF-8")).hexdigest() == user["password"]:
            user_obj = User(username)
            login_user(user_obj)
            return redirect(url_for("dashboard"))
        else:
            flash("Login failed", "error")
    return render_template("login.html", form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for(".login"))


# ------------------------------ Helper Methods ------------------------------ #

def get_flags(uid: str) -> dict:
    table = dynamodb.Table("CareerDay_Flags")
    response = table.get_item(
        Key = {
            "uid": uid
        })
    item = response["Item"]
    item["Flag"] = (hashlib.md5(item["Flag"].encode("UTF-8")).hexdigest())
    return item

def get_user_data(username: str) -> dict:
    try:
        table = dynamodb.Table("CareerDay_UserData")
        response = table.get_item(
            Key = {
                "username": username
            })
        return response["Item"]
    except:
        return []


def update_user(username: str, solved_flags: list) -> None:
    table = dynamodb.Table("CareerDay_UserData")
    table.update_item(
        Key={
            'username': username,
            'FlagsSolved': solved_flags
        },
        UpdateExpression='SET age = :val1',
        ExpressionAttributeValues={
            ':val1': 26
        })
