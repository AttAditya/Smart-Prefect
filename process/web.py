from process.quickfunctions import f
import flask
import logging
import threading

flask_logger = logging.getLogger("werkzeug")
flask_logger.level = logging.ERROR

app_kwargs = {"static_url_path": '/resource', "static_folder": 'resources'}
app = flask.Flask("Smart Prefect Website", **app_kwargs)


@app.route("/")
def home():
    return f("web/index.html")


@app.route("/log_in")
def log_in():
    return f("web/log-in.html")


def start():
    thread_kwargs = {
        "target": app.run,
        "kwargs": {
            "host": "0.0.0.0",
            "port": "2022"
        }
    }
    if not(f("token")):
        web_thread = threading.Thread(**thread_kwargs)
        web_thread.start()
    if f("webdev"):
        thread_kwargs["kwargs"] = {"port": "3000"}
        web_thread = threading.Thread(**thread_kwargs)
        web_thread.start()
