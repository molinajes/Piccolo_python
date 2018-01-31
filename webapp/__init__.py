import logging

from flask import current_app, Flask, redirect, render_template, request, url_for


def create_app(config, debug=False, testing=False, config_overrides=None, is_dev=False):
    app = Flask(__name__)
    app.config.from_object(config)

    app.debug = debug
    app.testing = testing

    if config_overrides:
        app.config.update(config_overrides)

    # Configure logging
    if not app.testing:
        logging.basicConfig(level=logging.INFO)

    #if not is_dev:
        #@app.before_request
        #def before_request():
            #if request.headers.get('X-Forwarded-Proto', 'http') != 'https':
              #  url = request.url.replace('http://', 'https://', 1)
                #code = 301
                #return redirect(url, code=code)

    @app.route("/")
    def index():
        return render_template("home.html")

    @app.route("/beta")
    def yc():
        return render_template("yc_home.html")

    @app.route("/contact")
    def yc_contact():
        return render_template("yc_contact.html")

    @app.route("/thoughts")
    def yc_thought():
        return render_template("yc_thought.html")

    @app.route("/yc_submit", methods=['POST'])
    def yc_submit():
        inputString = request.form['name']
        inputString = request.form['email']
        inputString = request.form['devices']
        inputString = request.form['location']
        return render_template("yc.html")

    # Add an error handler. This is useful for debugging the live application,
    # however, you should disable the output of the exception for production
    # applications.
    @app.errorhandler(500)
    def server_error(e):
        return 'An internal error occurred: <pre>{}</pre>. See logs for full stacktrace.'.format(e), 500

    return app
