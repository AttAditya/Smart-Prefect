from modules import logging, flask
from process.quickfunctions import f

flask_logger = logging.getLogger("werkzeug")
flask_logger.level = logging.ERROR

app_kwargs = {
    "static_url_path": "/resources",
    "static_folder": "resources",
    "template_folder": "web"
}
app = flask.Flask("Smart Prefect Website", **app_kwargs)

@app.route("/")
def home():
    return f("web/index.html")

@app.route("/invite")
def invite():
    return f("web/invite.html")

if __name__ == "__main__":
    app.run(port=3000)

