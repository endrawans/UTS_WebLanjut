from flask import Blueprint, request, jsonify
import controllers.matakuliah_controller as ctrl

mk_bp = Blueprint("matakuliah", __name__)

@mk_bp.get("/")
def get_all():
    return jsonify(ctrl.get_all())

@mk_bp.get("/<int:id>")
def get_by_id(id):
    return jsonify(ctrl.get_by_id(id))

@mk_bp.post("/")
def create():
    return jsonify(ctrl.create(request.json))

@mk_bp.put("/<int:id>")
def update(id):
    return jsonify(ctrl.update(id, request.json))

@mk_bp.delete("/<int:id>")
def delete(id):
    return jsonify({"deleted": ctrl.delete(id)})
