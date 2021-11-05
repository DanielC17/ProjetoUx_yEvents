from application import app
from flask import Flask, render_template, url_for, redirect
from application.model.entity.evento import Evento
from application.model.dao.eventoDao import EventoDAO

evento_lista=EventoDAO([
    Evento("Summer Party", "SP", "01/02", "4h", 'img/evento2.png'),
    Evento("Music Event", "MG", "14/07", "1H", 'img/evento3.png'),
    Evento("Hip-Hop", "RJ", "17/07", "7h", 'img/evento4.png'),
    Evento("Alok Eletro", "JF", "HOJE", "15h", 'img/evento1.png')   
])

@app.route("/")
def index():
    return render_template("eventos.html")

@app.route("/busca")
def busca():
    return render_template("busca.html")

@app.route('/busca')
def teste():
        return redirect(url_for('busca'))

@app.route("/calendario")
def calendario():
    return render_template("calendario.html")


@app.route("/user")
def user():
    return render_template("user.html")


@app.route("/lista_eventos")
def listar_eventos():
    return render_template("evento.html", evento_list=evento_lista.lista_eventos)