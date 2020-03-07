from flask import Flask, jsonify, request, Blueprint
from flask_cors import CORS
import logging


def create_app():
    app = Flask(__name__)
    CORS(
        app,
        origins=[r'http://localhost:8000'],
        supports_credentials=True,  # required if header 'credentials': 'include'
        # expose_headers='Authorization'  # doesn't seem to be required
    )

    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('flask_cors').level = logging.DEBUG

    api = Blueprint('API', __name__)
    # CORS(
    #     api,
    #     origins=[r'http://localhost:8000'],
    #     supports_credentials=True,  # required if header 'credentials': 'include'
    #     # expose_headers='Authorization'  # doesn't seem to be required
    # )

    @api.before_request
    def before_request():
        print(request.headers)
        if request.method == 'OPTIONS':
            # don't check auth
            return
        auth = request.headers.get('Authorization')
        print('*Authorization header:', auth)
        if auth != 'Bearer aaaa':
            raise ValueError

    @api.route('/api')
    def test():
        return jsonify({'data': 'It is working!'})

    app.register_blueprint(api)

    return app
