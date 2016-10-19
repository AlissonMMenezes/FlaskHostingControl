from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required
from db import db
from models.Identity import User, Role

user_datastore  = SQLAlchemyUserDatastore(db, User, Role)
security = Security()