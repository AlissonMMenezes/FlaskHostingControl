from flask import Flask, render_template
from commons.security_config import security, user_datastore, login_required
from blueprints.security.ExtendedRegisterForm import ExtendedRegisterForm
from blueprints.BlueprintRegister import BlueprintRegister
from blueprints.Packages import packages
from db import db
from models.Identity import User as UserModel
from models.FHCModel import Package as PackageModel

app = Flask(__name__)
app.secret_key = "super secret key"
register = BlueprintRegister()
register.init_app(app, ['.gitignore', 'BlueprintRegister', '__init__', 'security'])

app.config.from_object('instance.config.DevelopmentConfig')

security.init_app(app, user_datastore, register_form=ExtendedRegisterForm)

@app.route("/")
@login_required
def index():
    users = UserModel.query.all()
    return render_template("index.html",users=users)

@app.route("/customer/new")
@login_required
def new_customer():
    return render_template("new_customer.html")

if __name__ == "__main__":
    db.init_app(app)
    with app.app_context():
        db.create_all()
        app.run(host="0.0.0.0",debug=True,port=8000)
