#!/usr/bin/python

from flask import Blueprint, render_template

users = Blueprint('users',__name__)

@users.route("/users/new")
def new_user():
    return render_template("users/new.html")
