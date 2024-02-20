from app import db
from flask_login import UserMixin

class Clientes(db.Model,UserMixin):
    __tablename__ = 'cliente'
    idUsuario = db.Column(db.Integer, primary_key=True)
    NombreUsuario = db.Column(db.String(255))
    CorreoUsuario = db.Column(db.String(255))
    DireccionUsuario = db.Column(db.String(255))
    Telefono = db.Column(db.String(255))
    Contrasena = db.Column(db.String(255))
    ordenes = db.relationship("Ordenes", back_populates="clientes")
    def get_id(self):
        return str(self.idUsuario)
