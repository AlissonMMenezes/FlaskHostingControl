#!/usr/bin/python

from flask import Blueprint, render_template, request
from models.Identity import User as UserModel
from models.FHCModel import Package as PackageModel, ActivePackage
from commons.security_config import user_datastore, login_required
from db import db

users = Blueprint('users',__name__)

@users.route("/")
@login_required
def index():
    users = UserModel.query.all()
    print users[0].__dict__
    return render_template("index.html",users=users)

@users.route("/users/new/",methods=["GET"])
def new_user():
    packages = PackageModel.query.all()
    return render_template("users/new.html",packages=packages)

@users.route("/users/new/",methods=["POST"])
def add_user():    
    new_user = user_datastore.create_user(password=request.form['password'],
                                email=request.form['email'],
                                first_name=request.form['first_name'],
                                last_name=request.form['last_name'],
                                active=1)

    package = PackageModel.query.filter_by(id=request.form['package']).first()

    act_package = ActivePackage()
    act_package.backups = 0
    act_package.bandwidth = 0
    act_package.bash = package.bash
    act_package.cron_jobs = 0
    act_package.databases = 0
    act_package.dns_domains = 0
    act_package.dns_records = 0
    act_package.dns_template = ""
    act_package.mail_accounts = 0
    act_package.mail_domains = 0
    act_package.nameservers = ""
    act_package.package_id = package.id
    act_package.proxy_template = ""
    act_package.user_id = new_user.id
    act_package.web_aliases = 0
    act_package.web_domains = 0
    act_package.web_template = ""

    try:        
        db.session.add(act_package)
        db.session.commit()
        return render_template("users/new.html",message="User saved sucessfully")
    except Exception as e:
        db.session.rollback()
        return render_template("users/new.html",message="Failed to save new user: %s"%e)

@users.route("/users/<int:id>/", methods=['GET'])
def user(id):    
    user = UserModel.query.filter_by(id=id).first_or_404()
    packages = PackageModel.query.all()
    return render_template("users/show.html", user=user,packages=packages)

@users.route("/users/<int:id>/", methods=['POST'])
def user_save(id):
    packages = PackageModel.query.all()
    user = user_datastore.find_user(id=id)   
    try:
        if request.form['password'] != '':
            user.password = request.form['password']

        user.email = request.form['email']
        user.package = request.form['package']
        user.first_name = request.form['first_name']
        user.last_name = request.form['last_name']

        db.session.commit()
        return render_template("users/show.html",user=user, packages=packages,message="User saved sucessfully")
        
    except Exception as e:
        db.session.rollback()
        return render_template("users/show.html",user=user, packages=packages,message="Failed to save new user: %s"%e)

    
            