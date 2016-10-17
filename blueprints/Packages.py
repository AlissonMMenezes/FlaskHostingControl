#!/usr/bin/python

from flask import Blueprint, render_template

packages = Blueprint('packages',__name__)

@packages.route("/packages/")
def list_package():
    return render_template("packages/list.html")


@packages.route("/packages/new")
def new_package():
    return render_template("packages/new.html")
