from flask import Flask, render_template, redirect, url_for, request
import re

app = Flask(__name__, static_url_path="")

clients = []

def subscribe(email):
    if not re.match("[^@]+@[^@]+\.[^@]+", email):
        return False

    return True


@app.route("/", methods=["GET", "POST"])
def home_page():
    return render_template("index.html")


@app.route("/sub", methods=["GET", "POST"])
def subscribe_page():
    if request.method == "POST":
        email = request.form.get("email", "")
        hasSubbed = subscribe(email)
        if hasSubbed:
            return "true"
        else:
            return "", 400


@app.route("/msg", methods=["GET", "POST"])
def message_page():
    if request.method == "POST":
        email = request.form.get("email", "")
        hasSubbed = subscribe(email)
        if hasSubbed:
            return "true"
        else:
            return "", 400


if __name__ == "__main__":
    app.run()


