#!/usr/bin/python

from flask import Blueprint, render_template, request, redirect
from models.FHCModel import Package
from utils.FormUtil import form_to_instance
from db import db

packages = Blueprint('packages',__name__)

@packages.route("/packages/")
def list_package():
    packages = Package.query.all()
    return render_template("packages/list.html", packages = packages)


@packages.route("/packages/new", methods=['GET'])
def new_package():
    return render_template("packages/new.html")

@packages.route("/packages/new", methods=['POST'])
def new_package_post():
    try:
        package = form_to_instance(request.form, Package())
        db.session.add(package)
        db.session.commit()
    except Exception as e:
        db.session.rollback()

    return redirect("/packages/")
