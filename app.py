import os

from flask import Flask, render_template

app = Flask(__name__)


# =========================================================
# PRODUTOS DA LOJA
#
# Para ADICIONAR um produto: copie um bloco { ... } inteiro,
# cole no fim da lista e troque os dados.
# A imagem precisa estar na pasta static/imagens.
# O preço é escrito com ponto (35.00), sem "R$".
# =========================================================
PRODUTOS = [
    {
        "nome": "Extensão Elétrica 10A Bivolt",
        "marca": "Prismatec",
        "categoria": "Eletrônicos",
        "descricao": (
            "Extensão elétrica de 10 metros, cor preta e 10A bivolt, ideal "
            "para ligar seus aparelhos com segurança e praticidade no dia a dia."
        ),
        "preco": 35.00,
        "imagem": "extensao.jpg",
    },
    {
        "nome": "Processador Manual de Alimentos 900ml",
        "marca": "Shock Imports",
        "categoria": "Casa",
        "descricao": (
            "O Processador Manual de Alimentos 900ml da Shock Imports é um "
            "utensílio indispensável para agilizar o preparo de receitas."
        ),
        "preco": 35.00,
        "imagem": "processador.jpg",
    },
    {
        "nome": "Secador de Cabelo Bee Electrics HD-3201",
        "marca": "Bee Electrics",
        "categoria": "Beleza",
        "descricao": (
            "Secador de cabelo compacto para uso doméstico, com potência "
            "de 1600W e voltagem de 127V."
        ),
        "preco": 85.00,
        "imagem": "secador.jpg",
    },
    {
        "nome": "Jogo de Talheres 25 Peças IDee Home",
        "marca": "IDee Home",
        "categoria": "Móveis e Decoração",
        "descricao": (
            "Jogo de talheres com 25 peças, combinando aço inoxidável e "
            "cabos plásticos ergonômicos."
        ),
        "preco": 45.00,
        "imagem": "talheres.jpg",
    },
]


# TRANSFORMA 35.0 EM "R$ 35,00" (usado nos templates: {{ preco | brl }})
@app.template_filter("brl")
def formatar_real(valor):
    texto = f"{valor:,.2f}"
    texto = texto.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {texto}"


# PÁGINA INICIAL (mostra os 4 primeiros produtos como destaque)
@app.route("/")
def inicio():
    return render_template("index.html", produtos=PRODUTOS[:4])


# PÁGINA DE PRODUTOS (mostra todos)
@app.route("/produtos")
def produtos():
    return render_template("produtos.html", produtos=PRODUTOS)


# PÁGINA SOBRE NÓS
@app.route("/sobre")
def sobre():
    return render_template("sobre.html")


# PÁGINA DE CONTATO
@app.route("/contato")
def contato():
    return render_template("contato.html")


# PÁGINA 404 (endereço que não existe)
@app.errorhandler(404)
def pagina_nao_encontrada(erro):
    return render_template("404.html"), 404


# EXECUÇÃO DO SERVIDOR (no seu computador)
# O modo "debug" só liga se você pedir. Na internet ele fica DESLIGADO,
# porque mostra detalhes do código para qualquer visitante.
# Para ligar no seu PC: no PowerShell, rode  $env:FLASK_DEBUG="1"  e depois  python app.py
if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG") == "1")
