from app.main import bp as bp
from app.main.forms import FlagForm
from flask import redirect, current_app, render_template, flash, url_for, request
import boto3
import hashlib

dynamodb = boto3.resource("dynamodb")

@bp.route("/", methods=["GET", "POST"])
def index():
    # flash("Flask app successfully loaded", "success")
    # flash("Error while loading the Flask app", "error")

    forms = []

    form_flag_one = FlagForm()
    form_flag_two = FlagForm()

    forms.append(form_flag_one)

    if form_flag_one.validate_on_submit():
        flag_one = (hashlib.md5(form_flag_one.flag.data.encode("UTF-8")).hexdigest())
        correct_flag = get_table_item("2")
        print(flag_one)
        print(correct_flag["Flag"])
        if str(flag_one) == str(correct_flag["Flag"]):
            flash("Success", "success")
        else:
            flash("Not correct", "error")
        return render_template("main.html", forms=forms, flag_one=flag_one, correct_flag=correct_flag["Flag"])

    return render_template("main.html", forms=forms)

def get_table_item(uid: str):
    table = dynamodb.Table("CareerDay_Flags")
    response = table.get_item(
        Key={
            "uid": uid
        }
    )
    item = response["Item"]
    item["Flag"] = (hashlib.md5(item["Flag"].encode("UTF-8")).hexdigest())
    return item