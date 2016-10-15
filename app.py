from flask import Flask, render_template

app = Flask(__name__)

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
    app.run(host="0.0.0.0",debug=True)
