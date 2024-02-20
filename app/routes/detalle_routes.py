from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.DetallesOrdenes import DetallesOrdenes
from app import db

bp = Blueprint('Detalle', __name__)

@bp.route('/Detalle')
def index():
    data = DetallesOrdenes.query.all()

    return render_template('detalle/index.html', data=data)

@bp.route('/Detalle/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        cantidad = request.form['cantidad']
        total = request.form['total']
        orden = request.form['orden']
        producto = request.form['producto']

        new_detalle = DetallesOrdenes(Cantidad=cantidad,Total=total,Orden=orden,Producto=producto)
        db.session.add(new_detalle)
        db.session.commit()
        
        return redirect(url_for('Detalle.index'))

    return render_template('Detalle/add.html')

@bp.route('/Detalle/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    detalle = DetallesOrdenes.query.get_or_404(id)

    if request.method == 'POST':
        detalle.cantidad = request.form['cantidad']
        detalle.total = request.form['total']
        detalle.orden = request.form['orden']
        detalle.producto = request.form['producto']


        db.session.commit()
        return redirect(url_for('Detalle.index'))

    return render_template('detalle/edit.html', detalle=detalle)
    

@bp.route('/Detalle/delete/<int:id>')
def delete(id):
    detalle = DetallesOrdenes.query.get_or_404(id)
    
    db.session.delete(detalle)
    db.session.commit()

    return redirect(url_for('detalle.index'))