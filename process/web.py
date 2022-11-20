from process.quickfunctions import f
from modules import threading, logging, flask

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

app_thread = threading.Thread(
    target=app.run,
    kwargs={
        "host": "0.0.0.0"
    }
)

