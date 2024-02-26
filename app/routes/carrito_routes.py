from flask import Blueprint, render_template, redirect, url_for, request, flash
from app.models.Productos import Productos
from app.models.Carrito import Carrito

bp = Blueprint('carritos', __name__)
carrito_compras = Carrito()

@bp.route('/ListarCarrito')
def listar():
    items = carrito_compras.getItems()
    return render_template('productos/List.html', items=items)

@bp.route('/ListarProductos')
def index():
    productos = carrito_compras
    return render_template('index.html', productos=productos)

@bp.route('/agregar/<int:id>', methods=['POST' , 'GET' ])
def agregar_al_carrito(id):
    
    cantidad = int(request.form.get('cantidad', 1))
    carrito_compras.agregar_producto(id, cantidad)
    
    return render_template('shop.html')
    #return "Entra a agregar corrito"

@bp.route('/realizar_compra')
def realizar_compra():
    total = carrito_compras.calcular_total()
    return render_template('realizar_compra.html', total=total)

@bp.route('/generar_factura', methods=['POST'])
def generar_factura():
    total = carrito_compras.calcular_total()
    # Aquí puedes almacenar la información en la base de datos (crear registros en Carrito y Factura)
    # y luego limpiar el carrito de compras
    carrito_compras.carrito = []
    return render_template('factura.html', total=total)

@bp.route('/itemscarrito', methods=['GET', 'POST'])
def tCarrito():
    a = carrito_compras.tamanoD()
    print("Entra a carrito rutas", a)
    return carrito_compras.tamanoD()