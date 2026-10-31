import json
import os

from flask import Flask, jsonify, render_template, request

import target


app = Flask(__name__)

FUNCTIONS = {
    name: getattr(target, name)
    for name in (
        "is_adult",
        "celsius_to_fahrenheit",
        "count_vowels",
        "invert",
        "greet",
        "find_max",
        "get_price",
        "swap",
        "common_items",
        "is_leap_year",
        "to_int",
        "divide",
        "power",
        "square_root",
        "factorial",
        "average",
    )
}


def _decode_value(value):
    if not isinstance(value, dict) or set(value) != {"type", "value"}:
        return value
    value_type = value["type"]
    decoded = value["value"]
    if value_type == "none":
        return None
    if value_type == "tuple":
        return tuple(decoded)
    if value_type == "set":
        return set(decoded)
    if value_type == "json":
        return json.loads(decoded)
    return decoded


def _decode_arguments(payload):
    if not isinstance(payload, dict) or not isinstance(payload.get("args"), list):
        raise ValueError("request body must contain an 'args' list")
    return [_decode_value(value) for value in payload["args"]]


def _jsonable(value):
    if isinstance(value, (tuple, set)):
        return [_jsonable(item) for item in value]
    if isinstance(value, list):
        return [_jsonable(item) for item in value]
    if isinstance(value, dict):
        return {str(key): _jsonable(item) for key, item in value.items()}
    return value


def _commit_sha():
    return os.environ.get("COMMIT_SHA", os.environ.get("GITHUB_SHA", "local"))


@app.get("/")
def index():
    return render_template("index.html", functions=list(FUNCTIONS))


@app.get("/health")
def health():
    return jsonify(status="healthy", commit_sha=_commit_sha())


@app.post("/api/functions/<name>")
def execute_function(name):
    function = FUNCTIONS.get(name)
    if function is None:
        return jsonify(error="unknown function"), 404
    try:
        arguments = _decode_arguments(request.get_json(silent=True))
        result = function(*arguments)
        return jsonify(ok=True, result=_jsonable(result), result_type=type(result).__name__)
    except (
        TypeError,
        ValueError,
        KeyError,
        ZeroDivisionError,
        AttributeError,
        OverflowError,
    ) as exc:
        return jsonify(ok=False, error=str(exc), error_type=type(exc).__name__), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "5000")))
