"""数据库初始化：创建表并插入示例数据"""
from app import create_app
from models import db, Room, Seat


def init_database():
    app = create_app()
    with app.app_context():
        db.create_all()

        if Room.query.first():
            print("数据库已有数据，跳过初始化")
            return

        rooms_data = [
            {"name": "A101 自习室", "location": "教学楼A栋1层", "capacity": 20},
            {"name": "B202 自习室", "location": "教学楼B栋2层", "capacity": 16},
            {"name": "C303 阅览室", "location": "图书馆3层", "capacity": 12},
        ]

        for room_data in rooms_data:
            room = Room(**room_data)
            db.session.add(room)
            db.session.flush()

            cols = 5
            rows = (room_data["capacity"] + cols - 1) // cols
            for r in range(1, rows + 1):
                for c in range(1, cols + 1):
                    seat_num = (r - 1) * cols + c
                    if seat_num > room_data["capacity"]:
                        break
                    seat = Seat(
                        room_id=room.id,
                        seat_no=f"{r}-{c}",
                        row=r,
                        col=c,
                    )
                    db.session.add(seat)

        db.session.commit()
        print(f"初始化完成：创建了 {len(rooms_data)} 个自习室及其座位")


if __name__ == "__main__":
    init_database()
