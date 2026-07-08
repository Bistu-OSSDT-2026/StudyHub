from flask import Blueprint, jsonify, request
from datetime import date, timedelta
from sqlalchemy import func
from models import db, Booking, Seat, Room

stats_bp = Blueprint("stats", __name__)


@stats_bp.route("/overview", methods=["GET"])
def overview():
    """总体概览数据"""
    total_rooms = Room.query.count()
    total_seats = Seat.query.count()
    today = date.today()
    today_bookings = Booking.query.filter_by(date=today, status="active").count()
    total_bookings = Booking.query.count()

    return jsonify({
        "total_rooms": total_rooms,
        "total_seats": total_seats,
        "today_bookings": today_bookings,
        "total_bookings": total_bookings,
    })


@stats_bp.route("/by-room", methods=["GET"])
def bookings_by_room():
    """各自习室预约数量"""
    results = db.session.query(
        Room.name,
        func.count(Booking.id)
    ).join(Seat, Seat.room_id == Room.id
    ).join(Booking, Booking.seat_id == Seat.id
    ).filter(Booking.status == "active"
    ).group_by(Room.name).all()

    return jsonify([
        {"room_name": name, "booking_count": count}
        for name, count in results
    ])


@stats_bp.route("/daily-trend", methods=["GET"])
def daily_trend():
    """最近7天每日预约趋势"""
    days = int(request.args.get("days", 7))
    end_date = date.today()
    start_date = end_date - timedelta(days=days - 1)

    results = db.session.query(
        Booking.date,
        func.count(Booking.id)
    ).filter(
        Booking.date >= start_date,
        Booking.date <= end_date,
        Booking.status == "active"
    ).group_by(Booking.date).all()

    date_count = {str(d): c for d, c in results}
    trend = []
    for i in range(days):
        d = start_date + timedelta(days=i)
        trend.append({
            "date": d.isoformat(),
            "count": date_count.get(str(d), 0)
        })

    return jsonify(trend)
