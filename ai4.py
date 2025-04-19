from flask import Flask, render_template, request
import wikipedia
wikipedia.set_lang("de")

app = Flask(__name__)

# Speichert gesehene Begriffe
gelerntes = {}

@app.route("/", methods=["GET", "POST"])
def home():
    antwort = ""
    if request.method == "POST":
        frage = request.form["frage"].lower().strip()

        if frage.startswith("was heißt") or frage.startswith("was bedeutet"):
            begriff = frage.replace("was heißt", "").replace("was bedeutet", "").strip()
            if begriff in gelerntes:
                antwort = f"Ich weiß es schon! {gelerntes[begriff]}"
            else:
                try:
                    summary = wikipedia.summary(begriff, sentences=1, auto_suggest=False)
                    gelerntes[begriff] = summary
                    antwort = f"Ich habe es gefunden! {summary}"
                except Exception as e:
                    antwort = f"Leider konnte ich nichts dazu finden. ({e})"
        else:
            antwort = "Frag mich z. B.: 'Was heißt Toastbrot?' 😉"

    return render_template("botfred.html", antwort=antwort)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
