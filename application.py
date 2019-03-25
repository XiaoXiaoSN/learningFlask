import os
from flask import Flask, render_template

def create_app(config=None):
    """create a flask application object. and setting the application route."""
    app = Flask(__name__)    
    if config is not None:
        app.config.from_object(config)
    # else:
    #     print(os.environ['APP_SETTINGS'])
    #     app.config.from_object(os.environ['APP_SETTINGS'])

    # enter your route here  
    @app.route('/')
    def example():
        """ a example funciton """
        return 'hello world'

    # regiset buleprint

    # error handle
    @app.errorhandler(404)
    def not_found(error):
        return render_template('error/status404.html', title="404"), 404

    return app
