from application import app
from flask import Flask, render_template, url_for, redirect

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


