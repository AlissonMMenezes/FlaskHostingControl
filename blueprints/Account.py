#!/usr/bin/python

from flask import Flask, Blueprint, render_template, request
from flask_login import LoginManager
from commons.security_config import user_datastore
from db import db

account = Blueprint("account", __name__)

@account.route("/login2/")
def login():
    return render_template("account/login.html")
    
@account.route("/user/create/", methods=["GET"])
def create():
    return render_template("security/register_user.html")
    
@account.route("/user/create/", methods=["POST"])
def create_post():
    user_datastore.create_user(
            first_name = request.form["first_name"],
            last_name = request.form["last_name"],
            email = request.form["email"],
            password = request.form["password"])
            
    db.session.commit()
    