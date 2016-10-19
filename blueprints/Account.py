#!/usr/bin/python

from flask import Flask, Blueprint, render_template

account = Blueprint("account", __name__)

@account.route("/login/")
def login():
    return render_template("account/login.html")