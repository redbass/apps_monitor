from flask import Flask


def test_200():
    return "", 200


def test_400():
    return "", 400


def test_500():
    return "", 500


def create_roots(app):
    app.add_url_rule("/200", "200", test_200)
    app.add_url_rule("/400", "400", test_400)
    app.add_url_rule("/500", "500", test_500)


def create_app():
    app = Flask("Monitor Mock")
    create_roots(app)
    app.run(port=5001, debug=True)


if __name__ == "__main__":
    create_app()
