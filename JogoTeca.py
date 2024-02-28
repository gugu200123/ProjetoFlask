from flask import Flask, render_template

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


app = Flask(__name__)


@app.route('/inicio')
def ola():
    jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
    jogo2 = Jogo('Dota 2', 'Moba', 'PC')
    jogo3 = Jogo('God Of War', 'Ação', 'PS4')

    lista = [jogo1, jogo2, jogo3]
    return render_template('lista.html', titulo_da_pagina_inicio='Jogos', jogos=lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo jogo')
app.run()
