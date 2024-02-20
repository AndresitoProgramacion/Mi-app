from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.Productos import Productos
from app import db

bp = Blueprint('Producto', __name__)


@bp.route('/Producto')
def index():
    data = Productos.query.all()

    return render_template('index.html', data=data)

@bp.route('/Producto/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombre = request.form['nombre']
        marca = request.form['marca']
        descripcion = request.form['descripcion']
        precio = request.form['precio']
        new_producto = Productos(Nombre=nombre,Marca=marca,Descripcion=descripcion,Precio=precio)
        db.session.add(new_producto)
        db.session.commit()
        
        return redirect(url_for('producto.index'))

    return render_template('Producto/add.html')

@bp.route('/Producto/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    producto = Productos.query.get_or_404(id)

    if request.method == 'POST':
        producto.nombre = request.form['nombre']
        producto.marca = request.form['marca']
        producto.descripcion = request.form['descripcion']
        producto.precio = request.form['precio']
    


        db.session.commit()
        return redirect(url_for('Producto.index'))

    return render_template('producto/edit.html', producto=producto)
    

@bp.route('/Producto/delete/<int:id>')
def delete(id):
    producto = Productos.query.get_or_404(id)
    
    db.session.delete(producto)
    db.session.commit()

    return redirect(url_for('producto.index'))