from flask import Flask
from app.routes import bp as routes_blueprint
from app.dao.database import initialize_database
from scheduler.fetch_data import fetch_and_store_data
from scheduler.scheduler import schedule_fetch_and_store_data
from apscheduler.schedulers.background import BackgroundScheduler


def create_app():
    app = Flask(__name__)
    initialize_database()
    app.register_blueprint(routes_blueprint , url_prefix='/api')
    fetch_and_store_data()
    start_scheduler()
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)


def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(schedule_fetch_and_store_data, 'interval', hours=1)
    scheduler.start()