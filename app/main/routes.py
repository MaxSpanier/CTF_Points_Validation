from app.main import bp as bp
from app.main import login_manager
from app.main.forms import FlagForm, LoginForm
from app.main.models import User
from flask import redirect, current_app, render_template, flash, url_for, request
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
import boto3
import hashlib
import bcrypt

# DynamoDB setup
dynamodb = boto3.resource("dynamodb")
# test-user -- 1q2w3e4r5t

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

@bp.route("/")
def index():
    return redirect(url_for(".login"))

@bp.route("/login")
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = get_user_date(username)
        if user and bcrypt.checkpw(password.encode("utf-8"), user["password"].value):
            user_obj = User(username)
            login_user(user_obj)
            return redirect(url_for("dashboard"))
        else:
            pass
    return render_template("login.html", form=form)

@bp.route("/dashboard")
@login_required
def dashboard():
    return f"Welcome {current_user.id}"

@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for(".login"))


# ------------------------------ Helper Methods ------------------------------ #

def get_flag(uid: str) -> dict:
    table = dynamodb.Table("CareerDay_Flags")
    response = table.get_item(
        Key = {
            "uid": uid
        })
    item = response["Item"]
    item["Flag"] = (hashlib.md5(item["Flag"].encode("UTF-8")).hexdigest())
    return item

def get_user_date(username: str) -> dict:
    table = dynamodb.Table("CareerDay_UserData")
    response = table.get_item(
        Key = {
            "username": username
        })
    return response["Item"]

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