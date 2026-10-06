from app.main import app

client = app.test_client()


def test_home():
    res = client.get("/")
    assert res.status_code == 200
    assert "message" in res.get_json()


def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.get_json() == {"status": "ok"}


def test_greet_default():
    res = client.get("/api/greet")
    assert res.get_json()["greeting"] == "Hello, World!"


def test_greet_with_name():
    res = client.get("/api/greet?name=Amrutha")
    assert res.get_json()["greeting"] == "Hello, Amrutha!"
