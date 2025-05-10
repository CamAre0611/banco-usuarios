import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from flask import Blueprint
from controller.usuario_controller import UsuarioController
from service.usuario_service import UsuarioService

RUTA_USUARIOS = os.path.abspath(os.path.join(os.path.dirname(__file__), 'database/usuarios.txt'))

usuarios_bp = Blueprint('usuarios', __name__)
usuario_service = UsuarioService(RUTA_USUARIOS)
usuario_controller = UsuarioController(usuario_service)

usuarios_bp.route('/usuarios', methods=['GET'])(usuario_controller.listar)
usuarios_bp.route('/usuarios', methods=['POST'])(usuario_controller.crear)
usuarios_bp.route('/usuarios/<username>', methods=['PUT'])(usuario_controller.actualizar)
usuarios_bp.route('/usuarios/<username>', methods=['DELETE'])(usuario_controller.eliminar)
