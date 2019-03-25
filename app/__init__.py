import os
from flask import Flask, render_template

def create_app(config=None):
    """create a flask application object. and setting the application route."""
    app = Flask(__name__, instance_relative_config=True)  
    if config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(config)

    @app.route('/api/health')
    def health():
        return 'ok', 200

    # regiset buleprint

    # error handle
    @app.errorhandler(404)
    def not_found(error):
        return render_template('error/status404.html', title="404"), 404

    return app
