#!/usr/bin/python

from flask import Blueprint, render_template, request
from models.Identity import User as UserModel
from models.FHCModel import Package as PackageModel
from db import db

users = Blueprint('users',__name__)

@users.route("/users/new/",methods=["GET"])
def new_user():
    packages = PackageModel.query.all()
    return render_template("users/new.html",packages=packages)

@users.route("/users/new/",methods=["POST"])
def add_user():
    new_user = UserModel()    
    new_user.password = request.form['password']
    new_user.email = request.form['email']
    new_user.package = request.form['package']
    new_user.first_name = request.form['first_name']
    new_user.last_name = request.form['last_name']
    try:
        db.session.add(new_user)
        db.session.commit()
        return render_template("users/new.html",message="User saved sucessfully")
    except Exception as e:
        db.session.rollback()
        return render_template("users/new.html",message="Failed to save new user: %s"%e)
            