from flask import Blueprint

bp=Blueprint('main',__name__)

from app.routes import cliente_routes
from app.routes import detalle_routes
from app.routes import orden_routes
from app.routes import producto_routes
from app.routes import registro_routes
from app.routes import carrito_routes
from app.routes import apple1_routes
