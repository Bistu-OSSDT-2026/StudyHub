from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Room(db.Model):
    """自习室"""
    __tablename__ = "rooms"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    location = db.Column(db.String(100))
    capacity = db.Column(db.Integer, default=20)
    open_time = db.Column(db.String(10), default="08:00")
    close_time = db.Column(db.String(10), default="22:00")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    seats = db.relationship("Seat", backref="room", lazy=True, cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "location": self.location,
            "capacity": self.capacity,
            "open_time": self.open_time,
            "close_time": self.close_time,
        }


class Seat(db.Model):
    """座位"""
    __tablename__ = "seats"

    id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.Integer, db.ForeignKey("rooms.id"), nullable=False)
    seat_no = db.Column(db.String(10), nullable=False)
    row = db.Column(db.Integer, nullable=False)
    col = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(10), default="available")

    def to_dict(self):
        return {
            "id": self.id,
            "room_id": self.room_id,
            "seat_no": self.seat_no,
            "row": self.row,
            "col": self.col,
            "status": self.status,
        }


class Booking(db.Model):
    """预约记录"""
    __tablename__ = "bookings"

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), nullable=False)
    seat_id = db.Column(db.Integer, db.ForeignKey("seats.id"), nullable=False)
    date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.String(5), nullable=False)
    end_time = db.Column(db.String(5), nullable=False)
    status = db.Column(db.String(10), default="active")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    seat = db.relationship("Seat", backref="bookings")

    def to_dict(self):
        return {
            "id": self.id,
            "user_name": self.user_name,
            "seat_id": self.seat_id,
            "seat_no": self.seat.seat_no if self.seat else None,
            "room_id": self.seat.room_id if self.seat else None,
            "room_name": self.seat.room.name if self.seat and self.seat.room else None,
            "date": self.date.isoformat(),
            "start_time": self.start_time,
            "end_time": self.end_time,
            "status": self.status,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }