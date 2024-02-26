from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.secret_key = os.urandom(24)
    app.config.from_object('config.Config')
    
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'Login.index'
    
    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        from .models.Clientes import Clientes
        return Clientes.query.get(int(user_id))


    
    

    from app.routes import cliente_routes,detalle_routes,orden_routes,producto_routes,login_routes,registro_routes,carrito_routes,apple1_routes
    app.register_blueprint(cliente_routes.bp)
    app.register_blueprint(detalle_routes.bp)
    app.register_blueprint(orden_routes.bp)
    app.register_blueprint(producto_routes.bp)
    app.register_blueprint(login_routes.bp)
    app.register_blueprint(registro_routes.bp)
    app.register_blueprint(carrito_routes.bp)
    app.register_blueprint(apple1_routes.bp)
    
    
    return app