from flask import Flask, render_template

app = Flask(__name__)


# PÁGINA INICIAL
@app.route("/")
def inicio():
    return render_template("index.html")


# PÁGINA DE PRODUTOS
@app.route("/produtos")
def produtos():
    return render_template("produtos.html")


# PÁGINA DE CONTATO
@app.route("/contato")
def contato():
    return render_template("contato.html")


# EXECUÇÃO DO SERVIDOR
if __name__ == "__main__":
    app.run(debug=True)
