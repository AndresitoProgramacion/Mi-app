from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.Productos import Productos
from app.models.Carrito import Carrito
from app import db

bp = Blueprint('bp_apple', __name__)


@bp.route('/apple')
def index():
    carrito_compras = Carrito()
    tamano = carrito_compras.tamanoD()

    return render_template('apple1.html', tamano_carrito=tamano)