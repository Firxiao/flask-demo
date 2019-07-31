import flask
from flask import Flask
from config import config
from .foo import foo
from .bar import bar


def create_app(env_name):
    app = Flask(__name__, static_folder='static', static_url_path='/static')  # type: Flask
    app.config.from_object(config[env_name])

    @app.route('/')
    def demo():
        return """
               this is demo:
               <a href="/foo">foo</a>
               <a href="/bar">bar</a>
        """

    # register foo
    app.register_blueprint(foo)
    # register bar
    app.register_blueprint(bar)

    return app

