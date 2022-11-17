from process.quickfunctions import f
import flask
import logging

flask_logger = logging.getLogger("werkzeug")
flask_logger.level = logging.ERROR

app_kwargs = {
    "static_url_path": '/resource',
    "static_folder": 'resources'
}
app = flask.Flask("Smart Prefect Website", **app_kwargs)

@app.route("/")
def home():
    return f("web/index.html")

app.run()

