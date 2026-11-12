# ---------------------------------------------------------------
#  Mon premier site Web avec Flask
# ---------------------------------------------------------------
#  Ce fichier est le "cerveau" de votre site : c'est lui qui
#  reçoit les demandes des navigateurs et qui fabrique les réponses.
#
#  Vous allez le compléter petit à petit, exercice après exercice.
#  Les consignes sont dans le dossier "exercices/".
# ---------------------------------------------------------------

from flask import Flask, render_template, request, redirect, abort, jsonify
from datetime import datetime
from zoneinfo import ZoneInfo

app = Flask(__name__)


# Une "route" associe une adresse (URL) à une fonction Python.
# Ici : quand quelqu'un visite la page d'accueil "/",
# Flask exécute la fonction accueil() et renvoie son résultat au navigateur.
@app.get("/")
def accueil():
    return render_template("accueil.html")


# ---------------------------------------------------------------
#  Ajoutez vos nouvelles routes ci-dessous 👇
# ---------------------------------------------------------------

@app.get("/presentation")
def presentation():
    return render_template(
        "presentation.html",
        prenom="Yz",
        nom="Ak",
        loisirs=["Sport", "Code", "Jeux vidéo"],
    )


@app.get("/bonjour/<prenom>")
def bonjour(prenom):
    return render_template("bonjour.html", prenom=prenom)


@app.get("/calcul")
def calcul():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    op = request.args.get("op", "plus")

    if op == "fois":
        resultat = a * b
        symbole = "×"
    elif op == "moins":
        resultat = a - b
        symbole = "−"
    elif op == "divise":
        resultat = a / b if b else 0
        symbole = "÷"
    else:
        resultat = a + b
        symbole = "+"

    return render_template(
        "calcul.html",
        a=a,
        b=b,
        op=op,
        symbole=symbole,
        resultat=resultat,
    )


@app.get("/formulaire")
def formulaire():
    return render_template("formulaire.html")


@app.route("/salut", methods=["GET", "POST"])
def salut():
    if request.method == "POST":
        prenom = request.form.get("prenom", "inconnu")
        ville = request.form.get("ville", "nulle part")
        couleur = request.form.get("couleur", "")
    else:
        prenom = request.args.get("prenom", "inconnu")
        ville = request.args.get("ville", "nulle part")
        couleur = request.args.get("couleur", "")

    return render_template("salut.html", prenom=prenom, ville=ville, couleur=couleur)


@app.get("/home")
def home():
    return redirect("/")


@app.get("/secret")
def secret():
    abort(403)


@app.get("/moi")
def moi():
    return render_template(
        "moi.html",
        ip=request.headers.get("X-Real-IP", request.remote_addr),
        navigateur=request.headers.get("User-Agent"),
        langues=request.headers.get("Accept-Language"),
        entetes=request.headers.items(),
    )


@app.errorhandler(404)
def page_introuvable(erreur):
    return render_template("404.html"), 404


@app.errorhandler(403)
def page_interdite(erreur):
    return render_template("403.html"), 403


@app.get("/api/heure")
def api_heure():
    maintenant = datetime.now(ZoneInfo("Europe/Paris"))
    return jsonify({
        "heure": maintenant.strftime("%H:%M:%S"),
        "date": maintenant.strftime("%d/%m/%Y"),
        "message": "Bonjour depuis mon API !",
    })


@app.get("/horloge")
def horloge():
    return render_template("horloge.html")


# ---------------------------------------------------------------
#  Ne pas modifier : utile seulement pour lancer le site
#  sur votre propre ordinateur (python flask_app.py)
# ---------------------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
