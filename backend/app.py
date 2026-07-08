# 后端API主程序 - Yinzichun开发
from flask import Flask
from flask_cors import CORS
from config import Config
from models import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    CORS(app)

    from routes.rooms import rooms_bp
    from routes.seats import seats_bp
    from routes.bookings import bookings_bp
    from routes.stats import stats_bp

    app.register_blueprint(rooms_bp, url_prefix="/api/rooms")
    app.register_blueprint(seats_bp, url_prefix="/api/seats")
    app.register_blueprint(bookings_bp, url_prefix="/api/bookings")
    app.register_blueprint(stats_bp, url_prefix="/api/stats")

    return app


if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True, host="0.0.0.0", port=5000)
