from flask import Flask, render_template
from flask_migrate import Migrate,MigrateCommand, Manager
from db import db
from commons.security_config import security, user_datastore

app = Flask(__name__)
app.config.from_object('instance.config.DevelopmentConfig')

db.init_app(app)
security.init_app(app, user_datastore)

migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command("db",MigrateCommand)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/customer/new")
def new_customer():
    return render_template("new_customer.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True,port=8080)
