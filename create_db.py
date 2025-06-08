from app import create_app, db
from app.models import Match

app = create_app()
with app.app_context():
    print("🔍 DB URI =", app.config["SQLALCHEMY_DATABASE_URI"])
    db.create_all()
    print("Tables created")
