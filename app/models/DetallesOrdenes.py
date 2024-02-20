from app import db

class DetallesOrdenes(db.Model):
    __tablename__ = 'detalle_orden'
    idDetallesOrden = db.Column(db.Integer,primary_key=True)
    Cantidad = db.Column(db.String(255))
    Total = db.Column(db.String(255))
    Orden_idOrden = db.Column(db.Integer, db.ForeignKey('orden.idOrden'))
    Producto_idProducto = db.Column(db.Integer, db.ForeignKey('producto.idProducto'))
    producto = db.relationship("Productos", back_populates="detalles")
    orden = db.relationship("Ordenes", back_populates="detalles")