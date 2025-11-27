from flask import Blueprint, request, jsonify
import controllers.dosen_controller as ctrl

dosen_bp = Blueprint("dosen", __name__)

@dosen_bp.get("/")
def get_all():
    return jsonify(ctrl.get_all())

@dosen_bp.get("/<int:id>")
def get_by_id(id):
    return jsonify(ctrl.get_by_id(id))

@dosen_bp.post("/")
def create():
    return jsonify(ctrl.create(request.json))

@dosen_bp.put("/<int:id>")
def update(id):
    return jsonify(ctrl.update(id, request.json))

@dosen_bp.delete("/<int:id>")
def delete(id):
    return jsonify({"deleted": ctrl.delete(id)})
