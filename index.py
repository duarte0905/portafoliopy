from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/habilidades")
def habilidades():
    return render_template("habilidades.html")

@app.route("/proyecto")
def proyecto():
    return render_template("proyecto.html")

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

@app.route("/mero" , methods=["POST"])
def mero():
    if request.method == "POST":
        nom = request.form['nombre']
        mail = request.form['email']
        return render_template("mensa.html", nombre=nom, email=mail)

if __name__ == "__main__":
    app.run()