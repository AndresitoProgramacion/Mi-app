from app import db

class Productos(db.Model):
    __tablename__ = 'producto'
    idProducto  = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(255))
    Marca = db.Column(db.String(255))
    Descripccion = db.Column(db.String(255))
    Precio = db.Column(db.String(255))
    detalles = db.relationship("DetallesOrdenes", back_populates="producto")