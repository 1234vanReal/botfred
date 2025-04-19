import wikipedia

# Sprache einstellen (deutsch)
wikipedia.set_lang("de")

# Einfacher Speicher für gesehene Begriffe
gedaechtnis = {}

def botfred(frage):
    frage = frage.lower().strip()

    # Prüfen, ob bereits im Gedächtnis
    if frage in gedaechtnis:
        return f"Ich weiß es schon! {gedaechtnis[frage]}"

    # Versuche von Wikipedia zu holen
    try:
        suchbegriff = frage.replace("was heißt", "").replace("was bedeutet", "").strip()
        if not suchbegriff:
            return "Bitte frag mich nach der Bedeutung von etwas."

        zusammenfassung = wikipedia.summary(suchbegriff, sentences=1)
        gedaechtnis[frage] = zusammenfassung
        return zusammenfassung

    except Exception as e:
        return f"Ich konnte leider nichts finden zu: {suchbegriff}."
