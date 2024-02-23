from flask import Blueprint, render_template, request, redirect, url_for, jsonify,flash
from app import db
from app.models.Clientes import Clientes
from flask_bcrypt import Bcrypt
from flask_login import current_user,login_user,login_required,logout_user

bp = Blueprint('Login', __name__)


@bp.route('/',methods=['GET', 'POST'])
def index():
    
    if request.method == 'POST':
        correo = request.form['correo']
        contraseña = request.form['password']
        
        user = Clientes.query.filter_by(CorreoUsuario=correo).first()
        bcrypt = Bcrypt()

        if user:
            password = user.Contrasena
            if bcrypt.check_password_hash(pw_hash=password,password=contraseña):
                login_user(user)
                flash("Login successful!", "success")
                return render_template('apple1.html')
        flash('Invalid credentials. Please try again.', 'danger')
    
    if current_user.is_authenticated:
        return render_template('apple1.html')
    return render_template("index.html")


@bp.route('/logout',methods=['GET', 'POST'])
@login_required
def logout():
    if current_user.is_authenticated:
        logout_user()
        flash('sesion cerrada.', 'info')
    return  render_template("index.html")



