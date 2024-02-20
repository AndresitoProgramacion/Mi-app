from app import db

class Ordenes(db.Model):
    __tablename__ = 'orden'
    idOrden = db.Column(db.Integer, primary_key=True)
    Dia = db.Column(db.String(255))
    Mes = db.Column(db.String(255))
    Año = db.Column(db.String(255))
    Total = db.Column(db.String(255))
    
    Cliente_idUsuario = db.Column(db.Integer,db.ForeignKey('cliente.idUsuario'))
    detalles = db.relationship("DetallesOrdenes", back_populates="orden")
    clientes = db.relationship("Clientes", back_populates="ordenes")
   