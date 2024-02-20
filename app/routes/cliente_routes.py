from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.Clientes import Clientes
from app import db

bp = Blueprint('Cliente', __name__)

@bp.route('/Cliente')
def index1():
    data = Clientes.query.all()

    return render_template('cliente/index.html', data=data)

@bp.route('/Cliente/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        direccion = request.form['direccional']
        telefono = request.form['telefono']
        new_cliente = Clientes(NombreUsuario=nombre,CorreoUsuario=correo,DireccionUsuario=direccion,TelefonoUsuario=telefono)
        db.session.add(new_cliente)
        db.session.commit()
        
        return redirect(url_for('Cliente.index'))

    return render_template('cliente/add.html')

@bp.route('/Cliente/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    cliente = Clientes.query.get_or_404(id)

    if request.method == 'POST':
        cliente.nombre = request.form['nombre']
        cliente.correo = request.form['correo']
        cliente.direccion = request.form['direccion']
        cliente.telefono = request.form['telefono']
    


        db.session.commit()
        return redirect(url_for('Cliente.index'))

    return render_template('cliente/edit.html', cliente=cliente)
    

@bp.route('/Cliente/delete/<int:id>')
def delete(id):
    cliente = Clientes.query.get_or_404(id)
    
    db.session.delete(cliente)
    db.session.commit()

    return redirect(url_for('cliente.index'))

@bp.route('/Cliente/About')
def show_about():
    return render_template('about.html')

@bp.route('/Cliente/Inicio')
def show_Inicio():
    return render_template('apple1.html')

@bp.route('/Cliente/Compras')
def show_Comprar():
    return render_template('apple1.html')

@bp.route('/Cliente/Compras')
def show_abouts():
    return render_template('apple1.html')

@bp.route('/Cliente/shop')
def show_shop():
    return render_template('shop.html')

@bp.route('/Cliente/shop')
def show_comprar():
    return render_template('shop.html')

@bp.route('/Cliente/shop')
def show_compras():
    return render_template('shop-single.html')