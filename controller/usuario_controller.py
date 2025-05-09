import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import request, jsonify
from service.usuario_service import UsuarioService

class UsuarioController:
    def __init__(self, service: UsuarioService):
        self.service = service

    def listar(self):
        users = self.service.get_all_users()
        return jsonify([u.to_dict() for u in users]), 200

    def crear(self):
        data = request.get_json()
        if self.service.create_user(data['username'], data['password'], data.get('role', 'usuario')):
            return jsonify({"message": "Usuario creado"}), 201
        return jsonify({"message": "Usuario ya existe"}), 409

    def actualizar(self, username):
        data = request.get_json()
        if self.service.update_user(username, data.get('password'), data.get('role')):
            return jsonify({"message": "Usuario actualizado"}), 200
        return jsonify({"message": "Usuario no encontrado"}), 404

    def eliminar(self, username):
        if self.service.delete_user(username):
            return jsonify({"message": "Usuario eliminado"}), 200
        return jsonify({"message": "Usuario no encontrado"}), 404
