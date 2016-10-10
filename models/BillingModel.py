from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command("db",MigrateCommand)

class Customers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.PasswordType)

class Invoices(db.Model):
    __tablename__ = "invoices"
    id = db.Column(db.Integer, primary_key=True)
    service = db.Column(db.Integer,db.ForeignKey("services.id"))
    send_date = db.Column(db.Date)
    expiration_date = db.Column(db.Date)

class Subscriptions(db.Model):
    __tablename__ = "subscriptions"
    id = db.Column(db.Integer, primary_key=True)
    service = db.Column(db.Integer,db.ForeignKey("services.id"))
    initial_date = db.Column(db.Date)
    end_date = db.Column(db.Date)

class Products(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    value = db.Column(db.Float)
    services = db.relationship("Services")

class Services(db.Model):
    __tablename__ = "services"
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer,db.ForeignKey("customers.id"))
    product_id = db.Column(db.Integer,db.ForeignKey("products.id"))
    contract_date = db.Column(db.Date)
    cancel_date = db.Column(db.Date)

if __name__ == "__main__":
    manager.run()
