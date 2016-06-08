from flask import Flask

from monitor.controllers import monitor_page, ping_endpoint


def create_roots(app):
    app.add_url_rule("/monitor", "monitor", monitor_page)
    app.add_url_rule("/ping", "ping", ping_endpoint)


def create_app():
    app = Flask("Monitor")
    create_roots(app)
    app.run(debug=True)


if __name__ == "__main__":
    create_app()
