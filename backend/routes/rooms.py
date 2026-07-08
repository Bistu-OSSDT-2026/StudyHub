from flask import Blueprint, jsonify, request
from models import db, Room

rooms_bp = Blueprint("rooms", __name__)


@rooms_bp.route("", methods=["GET"])
def get_rooms():
    """获取所有自习室列表"""
    rooms = Room.query.all()
    return jsonify([room.to_dict() for room in rooms])


@rooms_bp.route("/<int:room_id>", methods=["GET"])
def get_room(room_id):
    """获取单个自习室详情"""
    room = Room.query.get_or_404(room_id)
    return jsonify(room.to_dict())


@rooms_bp.route("", methods=["POST"])
def create_room():
    """创建自习室"""
    data = request.get_json()
    if not data or not data.get("name"):
        return jsonify({"error": "自习室名称不能为空"}), 400

    room = Room(
        name=data["name"],
        location=data.get("location", ""),
        capacity=data.get("capacity", 20),
    )
    db.session.add(room)
    db.session.commit()
    return jsonify(room.to_dict()), 201


@rooms_bp.route("/<int:room_id>", methods=["DELETE"])
def delete_room(room_id):
    """删除自习室"""
    room = Room.query.get_or_404(room_id)
    db.session.delete(room)
    db.session.commit()
    return jsonify({"message": "删除成功"})
