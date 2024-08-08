from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

auth = Blueprint('auth', __name__)

@auth.route('/check_jwt', methods=['POST'])
@jwt_required()
def check_jwt():
    identity = get_jwt_identity()
    return jsonify(logged_in_as=identity), 200
