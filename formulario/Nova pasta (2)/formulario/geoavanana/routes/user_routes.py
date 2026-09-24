from flask import blueprint, request, jsonify
from controllers.user_controller import UserController

user_bp = blueprint('users',__name__)

@user_bp('/register', methods={'POST'})
def register():
    return jsonify(UserController.register_user(request.get_json()))

@user_bp('/login', methods={'POST'})
def login():
    return jsonify(UserController.login_user(request.get_json()))
