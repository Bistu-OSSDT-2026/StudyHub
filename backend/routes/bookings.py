from flask import Blueprint, jsonify, request
from datetime import date
from models import db, Booking, Seat

bookings_bp = Blueprint("bookings", __name__)


@bookings_bp.route("", methods=["GET"])
def get_bookings():
    """查询预约列表"""
    user_name = request.args.get("user_name")
    target_date = request.args.get("date")

    query = Booking.query
    if user_name:
        query = query.filter_by(user_name=user_name)
    if target_date:
        query = query.filter_by(date=date.fromisoformat(target_date))

    bookings = query.order_by(Booking.created_at.desc()).all()
    return jsonify([b.to_dict() for b in bookings])


@bookings_bp.route("", methods=["POST"])
def create_booking():
    """创建预约"""
    data = request.get_json()

    required = ["user_name", "seat_id", "date", "start_time", "end_time"]
    for field in required:
        if field not in data:
            return jsonify({"error": f"缺少必填字段: {field}"}), 400

    seat = Seat.query.get(data["seat_id"])
    if not seat:
        return jsonify({"error": "座位不存在"}), 404

    # 检查时间冲突
    conflict = Booking.query.filter(
        Booking.seat_id == data["seat_id"],
        Booking.date == date.fromisoformat(data["date"]),
        Booking.status == "active",
        Booking.start_time < data["end_time"],
        Booking.end_time > data["start_time"],
    ).first()

    if conflict:
        return jsonify({
            "error": "该座位在此时间段已有预约",
            "conflict": conflict.to_dict()
        }), 409

    booking = Booking(
        user_name=data["user_name"],
        seat_id=data["seat_id"],
        date=date.fromisoformat(data["date"]),
        start_time=data["start_time"],
        end_time=data["end_time"],
    )
    db.session.add(booking)
    db.session.commit()

    return jsonify(booking.to_dict()), 201


@bookings_bp.route("/<int:booking_id>/cancel", methods=["PUT"])
def cancel_booking(booking_id):
    """取消预约"""
    booking = Booking.query.get_or_404(booking_id)
    if booking.status == "cancelled":
        return jsonify({"error": "预约已经取消"}), 400

    booking.status = "cancelled"
    db.session.commit()
    return jsonify({"message": "预约已取消", "booking": booking.to_dict()})
