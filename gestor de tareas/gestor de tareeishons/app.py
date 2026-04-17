from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/reg")
def registrar():
    return render_template("reg.html")

@app.route("/inicia")
def inicio_sesion():
    return render_template("inicia.html")

@app.route("/recuperar")
def recuperar_contraseña():
    return render_template("recuperar.html")

if __name__ == "__main__":
    app.run(debug=True)
