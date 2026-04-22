from src.app.main import app


def test_title_present():
    assert app.title == 'Smart City Traffic Forecast'
