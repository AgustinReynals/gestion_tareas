from flask import render_template,request,url_for,redirect,jsonify,Blueprint

auth_bp = Blueprint("AUTH",__name__)

@auth_bp.route("/login",methods=["POST","GET"])
def login():
    if request.method == "POST":
        datos = request.form
    return render_template("login.html")