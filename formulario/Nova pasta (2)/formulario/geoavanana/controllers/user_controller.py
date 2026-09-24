from workzeug.security import generate_password_hash, check_password
from flask_jwt_extended import create_access_token
from models.user_model import Usermodel

class UserController:

    @staticmethod
    def register_user(data):
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return("error": "Nome de usuário e senha são obrigatórios"), 400

        hashed_password = generate_password_hash(password)
        if UserModel.create_user(username, hashed_password):
            return("message": "usuário registrado com sucesso"),201

        return("error": "nome de usuario ja existe"),400