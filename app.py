from flask import Flask, render_template
from blueprints.Users import users
from blueprints.Packages import packages
from blueprints.Account import account
from blueprints.Admin import admin
from commons.security_config import security, user_datastore, login_required
from blueprints.security.ExtendedRegisterForm import ExtendedRegisterForm
from db import db

app = Flask(__name__)

app.register_blueprint(users)
app.register_blueprint(packages)
app.register_blueprint(account)
app.register_blueprint(admin)
app.secret_key = "super secret key"

app.config.from_object('instance.config.DevelopmentConfig')

security.init_app(app, user_datastore, register_form=ExtendedRegisterForm)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/customer/new")
@login_required
def new_customer():
    return render_template("new_customer.html")

if __name__ == "__main__":
    db.create_all()
    app.run(host="0.0.0.0",debug=True,port=8080)
