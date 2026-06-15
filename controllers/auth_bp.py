from flask import render_template,request,url_for,redirect,jsonify,Blueprint,flash
from models.auth import *
auth_bp = Blueprint("auth",__name__)

@auth_bp.route("/",methods=["POST","GET"])
def login():
    if request.method == "POST":
        datos = request.form
        if validarSesion(datos):
            return render_template("home.html")
        return redirect(url_for("auth.login"))
    return render_template("login.html")

@auth_bp.route("/register", methods=["POST","GET"])
def register():
    if request.method == "POST":
        datos = request.form
        if emailExistente(datos["email"]):
            if RegistrarUsuario(datos):
                return redirect(url_for("auth.login"))
            flash("algo salio mal")
            return redirect(url_for("auth.register"))
        flash("El email ya existe")
        return redirect(url_for("auth.register"))

    return render_template("registro.html")