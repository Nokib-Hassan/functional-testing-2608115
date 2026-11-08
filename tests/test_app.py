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


# Added


@pytest.mark.parametrize(
    ("environment", "expected"),
    [
        (
            {
                "RENDER_GIT_COMMIT": "render123",
                "COMMIT_SHA": "commit123",
                "GITHUB_SHA": "github123",
            },
            "render123",
        ),
        (
            {"COMMIT_SHA": "commit123", "GITHUB_SHA": "github123"},
            "commit123",
        ),
        ({"GITHUB_SHA": "github123"}, "github123"),
        ({}, "local"),
    ],
)
def test_health_commit_sha_fallbacks(client, monkeypatch, environment, expected):
    for key in ("RENDER_GIT_COMMIT", "COMMIT_SHA", "GITHUB_SHA"):
        monkeypatch.delenv(key, raising=False)

    for key, value in environment.items():
        monkeypatch.setenv(key, value)

    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {
        "status": "healthy",
        "commit_sha": expected,
    }


@pytest.mark.parametrize(
    "payload",
    [
        None,
        [],
        {},
        {"args": "18"},
        {"args": None},
    ],
)
def test_execute_function_rejects_invalid_payloads(client, payload):
    response = client.post("/api/functions/is_adult", json=payload)

    assert response.status_code == 400
    assert response.get_json()["ok"] is False
    assert response.get_json()["error_type"] == "ValueError"


def test_execute_function_decodes_none_value(client):
    response = client.post(
        "/api/functions/greet",
        json={"args": [{"type": "none", "value": None}]},
    )

    assert response.status_code == 200
    assert response.get_json() == {
        "ok": True,
        "result": "Hello, Guest!",
        "result_type": "str",
    }


def test_execute_function_decodes_json_value(client):
    response = client.post(
        "/api/functions/find_max",
        json={"args": [{"type": "json", "value": "[3, 9, 1]"}]},
    )

    assert response.status_code == 200
    assert response.get_json() == {
        "ok": True,
        "result": 9,
        "result_type": "int",
    }


def test_execute_function_handles_unknown_encoded_type(client):
    response = client.post(
        "/api/functions/to_int",
        json={"args": [{"type": "unknown", "value": "12"}]},
    )

    assert response.status_code == 200
    assert response.get_json()["result"] == 12


@pytest.mark.parametrize(
    ("name", "payload", "expected_error"),
    [
        ("is_adult", {"args": [-1]}, "ValueError"),
        ("count_vowels", {"args": [123]}, "TypeError"),
        ("greet", {"args": [123]}, "AttributeError"),
        ("is_adult", {"args": []}, "TypeError"),
    ],
)
def test_execute_function_returns_supported_errors(
    client, name, payload, expected_error
):
    response = client.post(f"/api/functions/{name}", json=payload)

    assert response.status_code == 400
    body = response.get_json()
    assert body["ok"] is False
    assert body["error_type"] == expected_error
    assert isinstance(body["error"], str)


def test_execute_function_rejects_invalid_json_encoding(client):
    response = client.post(
        "/api/functions/find_max",
        json={"args": [{"type": "json", "value": "not-valid-json"}]},
    )

    assert response.status_code == 400
    assert response.get_json()["error_type"] == "JSONDecodeError"


def test_unknown_function_returns_json_not_found(client):
    response = client.post("/api/functions/does_not_exist", json={"args": []})

    assert response.status_code == 404
    assert response.is_json
    assert response.get_json() == {"error": "unknown function"}


def test_static_frontend_assets_are_served(client):
    styles = client.get("/static/styles.css")
    script = client.get("/static/app.js")

    assert styles.status_code == 200
    assert styles.content_type.startswith("text/css")
    assert b".grid" in styles.data
    assert script.status_code == 200
    assert script.content_type.startswith("text/javascript")
    assert b"fetchWithTimeout" in script.data
