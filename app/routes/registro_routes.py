from app import db
from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models import Clientes
from flask_bcrypt import Bcrypt

bp = Blueprint('bp_registro', __name__)

@bp.route('/registro')
def index():

    return render_template('registro.html')

@bp.route('/registro/insertar', methods=['POST'])
def insertar():

     if request.method == 'POST':
        bcrypt = Bcrypt()
    
        nombre = request.form['nombre']
        correo = request.form['correo']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        contrasena = request.form['contrasena']
        hash_password = bcrypt.generate_password_hash(contrasena).decode("utf-8")
        new_cliente = Clientes(idUsuario=None,NombreUsuario=nombre,CorreoUsuario=correo,DireccionUsuario=direccion,Telefono=telefono,Contrasena=hash_password)
        db.session.add(new_cliente)
        db.session.commit()
        
        return redirect(url_for('Login.index'))

    

