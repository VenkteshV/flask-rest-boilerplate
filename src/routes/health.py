from datetime import datetime, timedelta
from flask import jsonify, abort, request, Blueprint

REQUEST_API = Blueprint('request_api', __name__)


def get_blueprint():
    """Return the blueprint for the main app module"""
    return REQUEST_API


MODEL_HEALTH = {
    "health": {
        'status': u'api is up',
        'timestamp': (datetime.today() - timedelta(1)).timestamp()
    },
}


@REQUEST_API.route('/health', methods=['GET'])
def get_health():
    """Return all book requests
    @return: 200: health of api\
    flask/response object with application/json mimetype.
    """
    return jsonify(MODEL_HEALTH)
