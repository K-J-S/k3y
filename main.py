from flask import Flask, render_template, redirect, url_for, request
import article

app = Flask(__name__, static_url_path="")

clients = []


@app.route("/", methods=["GET", "POST"])
def home_page():
    return render_template("index.html")


@app.route("/blog", methods=["GET", "POST"])
def blog_page():
    terms = article.get_keyterms()
    articles = article.get_articles()
    return render_template("blog.html", terms=terms, articles=articles)


if __name__ == "__main__":
    app.run()


