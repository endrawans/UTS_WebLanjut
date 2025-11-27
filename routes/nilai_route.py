from flask import Blueprint, request, jsonify
import controllers.nilai_controller as ctrl

nilai_bp = Blueprint("nilai", __name__)

@nilai_bp.get("/")
def get_all():
    return jsonify(ctrl.get_all())

@nilai_bp.get("/<int:id>")
def get_by_id(id):
    return jsonify(ctrl.get_by_id(id))

@nilai_bp.post("/")
def create():
    return jsonify(ctrl.create(request.json))

@nilai_bp.put("/<int:id>")
def update(id):
    return jsonify(ctrl.update(id, request.json))

@nilai_bp.delete("/<int:id>")
def delete(id):
    return jsonify({"deleted": ctrl.delete(id)})
