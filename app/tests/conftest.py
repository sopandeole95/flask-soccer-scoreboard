import pytest
from app import create_app, db


@pytest.fixture
def app():
    # Pass this in _before_ db.init_app is ever called
    test_conf = {
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
    }
    app = create_app(test_config=test_conf)

    # Create tables in the in-memory DB
    with app.app_context():
        db.create_all()
    yield app

    # Teardown
    with app.app_context():
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()
