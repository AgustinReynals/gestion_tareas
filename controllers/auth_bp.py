from flask import render_template,request,url_for,redirect,jsonify,Blueprint
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