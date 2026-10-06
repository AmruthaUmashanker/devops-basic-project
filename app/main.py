from flask import Flask, jsonify, request

app = Flask(__name__)


@app.get("/")
def home():
    return jsonify(message="Hello from my DevOps project!", version="1.0.0")


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.get("/api/greet")
def greet():
    name = request.args.get("name", "World")
    return jsonify(greeting=f"Hello, {name}!")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
