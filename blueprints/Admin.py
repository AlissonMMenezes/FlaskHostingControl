#!/usr/bin/python

from flask import Flask, Blueprint, render_template, request
from flask_login import LoginManager
from commons.security_config import user_datastore
from db import db

admin = Blueprint("admin", __name__, url_prefix="/admin")

@admin.route("/")
def index():
    return render_template("panel/index.html")