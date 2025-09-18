from flask import Blueprint, request, jsonify
from . import service

user_bp = Blueprint("user", __name__)

@user_bp.route("/", methods=["GET"])
def get_users():
    return jsonify(service.list_users())

@user_bp.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = service.get_user(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@user_bp.route("/", methods=["POST"])
def create_user():
    data = request.json
    user = service.create_user(data)
    return jsonify(user), 201

@user_bp.route("/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.json
    user = service.update_user(user_id, data)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@user_bp.route("/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    success = service.delete_user(user_id)
    if success:
        return jsonify({"message": "User deleted"})
    return jsonify({"error": "User not found"}), 404
