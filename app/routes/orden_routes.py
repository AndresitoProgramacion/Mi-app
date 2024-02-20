from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.Ordenes import Ordenes
from app import db

bp = Blueprint('Orden', __name__)

@bp.route('/Orden')
def index():
    data = Ordenes.query.all()

    return render_template('orden/index.html', data=data)

@bp.route('/Orden/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        dia = request.form['dia']
        mes = request.form['mes']
        año = request.form['año']
        total = request.form['total']
        
        cliente = request.form['cliente']
        new_orden = Ordenes(Dia=dia,Mes=mes,Año=año,Cliente=cliente)
        db.session.add(new_orden)
        db.session.commit()
        
        return redirect(url_for('Orden.index'))

    return render_template('orden/add.html')

@bp.route('/Orden/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    orden = Ordenes.query.get_or_404(id)

    if request.method == 'POST':
        orden.dia = request.form['dia']
        orden.mes = request.form['mes']
        orden.año = request.form['año']
        orden.cliente = request.form['cliente']
    


        db.session.commit()
        return redirect(url_for('Orden.index'))

    return render_template('orden/edit.html', orden=orden)
    

@bp.route('/Orden/delete/<int:id>')
def delete(id):
    orden = Ordenes.query.get_or_404(id)
    
    db.session.delete(orden)
    db.session.commit()

    return redirect(url_for('orden.index'))