from flask import Blueprint, request, jsonify
import controllers.kelas_controller as ctrl

kelas_bp = Blueprint("kelas", __name__)

@kelas_bp.get("/")
def get_all():
    return jsonify(ctrl.get_all())

@kelas_bp.get("/<int:id>")
def get_by_id(id):
    return jsonify(ctrl.get_by_id(id))

@kelas_bp.post("/")
def create():
    return jsonify(ctrl.create(request.json))

@kelas_bp.put("/<int:id>")
def update(id):
    return jsonify(ctrl.update(id, request.json))

@kelas_bp.delete("/<int:id>")
def delete(id):
    return jsonify({"deleted": ctrl.delete(id)})
