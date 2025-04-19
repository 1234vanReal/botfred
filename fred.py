# app.py

from flask import Flask, render_template, request
from ai4 import frage_bot

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    antwort = ""
    if request.method == "POST":
        user_input = request.form["frage"]
        antwort = frage_bot(user_input)
    return render_template("index.html", antwort=antwort)

if __name__ == "__main__":
    app.run(debug=True)