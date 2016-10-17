#!/usr/bin/python

from flask import Blueprint, render_template

packages = Blueprint('packages',__name__)

@packages.route("/packages/new")
def new_package():
    return render_template("packages/new.html")
