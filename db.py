from flask import Flask
from flask_sqlalchemy import SQLAlchemy,BaseQuery
from flask_migrate import Migrate,MigrateCommand, Manager

db = SQLAlchemy()
