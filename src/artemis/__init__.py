import os
from flask import (
    Flask,
    request,
    render_template,
    redirect,
    url_for,
    session,
    jsonify,
    send_file,
    flash,
    abort, g
)
import json_logging
import logging
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from flask_wtf.csrf import CSRFProtect

from artemis.repo.somedomain import SomedomainRepository
from artemis.domain import (
    SomedomainSchema
)
from artemis.persistence import PersistenceType


def create_app(test_config=None):
    app = Flask(__name__)
    csrf = CSRFProtect()

    if test_config:
        app.config["SECRET_KEY"] = test_config.get("SECRET_KEY")
    else:
        app.config["SECRET_KEY"] = os.getenv("ARTEMIS_SECRET_KEY")

    json_logging.CREATE_CORRELATION_ID_IF_NOT_EXISTS = True
    json_logging.init_flask(enable_json=True)
    json_logging.init_request_instrument(app, exclude_url_patterns=["/status"])
    logger = logging.getLogger("artemis")
    handler = logging.StreamHandler()
    log_level = os.getenv("LOG_LEVEL", "INFO")
    logger.setLevel(log_level)
    handler.setLevel(log_level)
    if handler not in logger.handlers:
        logger.addHandler(handler)

    sentry_dsn = os.getenv("SENTRY_DSN")
    if sentry_dsn:
        sentry_sdk.init(
            sentry_dsn,
            environment=os.getenv("ENVIRONMENT"),
            integrations=[FlaskIntegration()],
        )

    csrf.init_app(app)
    somedomain_repository = SomedomainRepository()
    persistence = PersistenceType.FILE.persistence()

    @app.route("/status", methods=["GET"])
    def status():
        return "Ok", 200

    @app.errorhandler(400)
    def bad_request(error):
        flash(error, 'error')
        return render_template('oops.html'), 400
    
    @app.errorhandler(401)
    def unauthorized(error):
        flash(error, 'error')
        return render_template('oops.html'), 401
    
    @app.errorhandler(403)
    def forbidden(error):
        flash(error, 'error')
        return render_template('oops.html'), 403
    
    @app.errorhandler(404)
    def page_not_found(error):
        flash(error, 'error')
        return render_template('oops.html'), 404
    
    @app.errorhandler(405)
    def method_not_allowed(error):
        flash(error, 'error')
        return render_template('oops.html'), 405
    
    @app.errorhandler(500)
    def server_error_handler(error):
        return render_template("oops.html"), 500

    return app
