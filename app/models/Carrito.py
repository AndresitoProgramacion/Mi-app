from flask import Blueprint, render_template, redirect, url_for, request, flash
from app.models.Productos import Productos


bp = Blueprint('carritos', __name__)

class Carrito:
    def __init__(self):
        self.carrito = []

    def agregar_producto(self, producto_id, cantidad):
        producto = Productos.query.get_or_404(producto_id)
        if producto:
            item = {'producto': producto, 'cantidad': cantidad}
            self.carrito.append(item)

    def calcular_total(self):
        return sum(item['producto'].Precio * item['cantidad'] for item in self.carrito)
    
    def tamanoD(self):   
        return len(self.carrito)

    def getItems(self):
        return self.carrito
    
    def vaciarcarrito(self):
        self.carrito = []
    