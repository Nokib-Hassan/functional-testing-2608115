import pytest

from app import app


@pytest.fixture()
def client():
    app.config.update(TESTING=True)
    with app.test_client() as test_client:
        yield test_client


def test_index_and_health(client, monkeypatch):
    monkeypatch.setenv("COMMIT_SHA", "abc123")
    page = client.get("/")
    health = client.get("/health")
    assert page.status_code == 200
    assert b"Functional Testing Lab" in page.data
    assert health.get_json() == {"status": "healthy", "commit_sha": "abc123"}


@pytest.mark.parametrize(
    ("name", "payload", "expected"),
    [
        ("is_adult", {"args": [18]}, {"ok": True, "result": True, "result_type": "bool"}),
        (
            "swap",
            {"args": [{"type": "tuple", "value": [1, 2]}]},
            {"ok": True, "result": [2, 1], "result_type": "tuple"},
        ),
        (
            "common_items",
            {
                "args": [
                    {"type": "set", "value": [1, 2]},
                    {"type": "set", "value": [2, 3]},
                ]
            },
            {"ok": True, "result": [2], "result_type": "set"},
        ),
    ],
)
def test_execute_function(client, name, payload, expected):
    response = client.post(f"/api/functions/{name}", json=payload)
    assert response.status_code == 200
    body = response.get_json()
    assert body["ok"] is True
    assert body["result_type"] == expected["result_type"]
    assert body["result"] == expected["result"]


def test_execute_function_error_unknown_and_bad_payload(client):
    error = client.post("/api/functions/divide", json={"args": [1, 0]})
    unknown = client.post("/api/functions/not_a_function", json={"args": []})
    bad_payload = client.post("/api/functions/is_adult", json={"args": "18"})
    assert error.status_code == 400
    assert error.get_json()["error_type"] == "ZeroDivisionError"
    assert unknown.status_code == 404
    assert bad_payload.status_code == 400
    assert bad_payload.get_json()["error_type"] == "ValueError"
