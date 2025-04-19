from flask import Flask, render_template, request
from ai4 import botfred  # Importiere deine Botfunktion aus ai4.py



@app.route("/", methods=["GET", "POST"])
def home():
    antwort = ""
    if request.method == "POST":
        frage = request.form["frage"]
        antwort = botfred(frage)  # Übergib die Frage an deinen Bot
    return render_template("index.html", antwort=antwort)

if __name__ == "__main__":
    app.run(debug=True)
    app = Flask(__name__, template_folder='templates')
