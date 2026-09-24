from flask import Flask
from flask_jwt_extended import JWTManager
from database.db import init_dp
from routes.user_routes import user_bp
from routes.formulário_routes import formulario_bp

app = Flask(__name__)

app.config.ftom.pyfile('config.py')

jwt = JWTManager(app)

init_dp()

app.register_blueprint(user_bp, url_prefix='users')
app.register_blueprint(formulario_bp, url_prefix='/formularios')

if __name__ == '_main_':
    app.run(debug=True)
    