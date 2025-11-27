from flask import Blueprint, request, jsonify
import controllers.mahasiswa_controller as ctrl

mahasiswa_bp = Blueprint("mahasiswa", __name__)

@mahasiswa_bp.get("/")
def get_all():
    return jsonify(ctrl.get_all())

@mahasiswa_bp.get("/<int:id>")
def get_by_id(id):
    return jsonify(ctrl.get_by_id(id))

@mahasiswa_bp.post("/")
def create():
    return jsonify(ctrl.create(request.json))

@mahasiswa_bp.put("/<int:id>")
def update(id):
    return jsonify(ctrl.update(id, request.json))

@mahasiswa_bp.delete("/<int:id>")
def delete(id):
    return jsonify({"deleted": ctrl.delete(id)})
