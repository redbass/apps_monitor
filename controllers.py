import os
from flask import json, request

import flask
import requests

from flask import render_template

REQUEST_TIMEOUT = 5000


def monitor_page():

    apps = _get_apps_json()
    return render_template("monitor.html", apps=apps)


def ping_endpoint():

    status_code = None
    app_id = request.args.get("appId")

    apps = _get_apps_json()

    app = next(app for app in apps if app["id"] == app_id)

    if app:
        try:
            response = requests.get(app['url'], timeout=REQUEST_TIMEOUT)
            status_code = response.status_code
        except Exception:
            status_code = "???"

    return flask.jsonify({
        "code": status_code
    })


def _get_apps_json():

    root_path = os.path.dirname(os.path.dirname(__file__))
    apps_path = os.path.join(root_path, "monitor/resources/apps.json")

    with open(apps_path) as jdata:
        japps = json.load(jdata)
        for app in japps:
            app['url'] = "http://%s" % app['host']
            if "port" in app:
                app['url'] += ":%s" % app['port']
            app['url'] += "/" + app['endpoint']

        return japps
