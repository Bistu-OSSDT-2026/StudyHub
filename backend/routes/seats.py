from flask import Blueprint, jsonify, request
from datetime import date
from models import db, Seat, Booking

seats_bp = Blueprint("seats", __name__)


@seats_bp.route("/room/<int:room_id>", methods=["GET"])
def get_seats_by_room(room_id):
    """获取某自习室的所有座位（含当日预约状态）"""
    target_date = request.args.get("date", date.today().isoformat())
    seats = Seat.query.filter_by(room_id=room_id).all()

    result = []
    for seat in seats:
        seat_data = seat.to_dict()
        active_bookings = Booking.query.filter(
            Booking.seat_id == seat.id,
            Booking.date == date.fromisoformat(target_date),
            Booking.status == "active"
        ).all()
        seat_data["bookings"] = [b.to_dict() for b in active_bookings]
        seat_data["is_booked"] = len(active_bookings) > 0
        result.append(seat_data)

    return jsonify(result)


@seats_bp.route("", methods=["POST"])
def create_seat():
    """添加座位"""
    data = request.get_json()
    seat = Seat(
        room_id=data["room_id"],
        seat_no=data["seat_no"],
        row=data.get("row", 1),
        col=data.get("col", 1),
    )
    db.session.add(seat)
    db.session.commit()
    return jsonify(seat.to_dict()), 201
