from flask import Flask, request, jsonify, Blueprint
from flask_jwt import JWT, jwt_required
from flask_cors import CORS
from functools import wraps
import src.config as cnf
import datetime
import src.utils.types as typesUtils
import src.utils.keywords as keywordsUtils
import src.utils.auth as authUtils
import src.utils.classification as classificationUtils
import src.utils.utils as Utils


app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SECRET_KEY'] = "123é&12332132112eDSDSqdfsqf@sdfQSBF__"
app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(days=10)
app.config['JWT_AUTH_URL_RULE'] = "/api/auth"

CORS(app, resources={r"/api/*": {"origins": "*"}})
JWT(app, authUtils.authenticate, authUtils.identity)

BP = Blueprint('burritos', __name__)


# -----------------------  Authentification ------------------------
def app_auth_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        credentials = None
        if ('KEY' in request.headers and 'SECRET' in request.headers):
            credentials = authUtils.app_auth_required(request)
        if (credentials):
            return f(*args, **kwargs)
        else:
            return jsonify("Auth Error"), 401
    return decorated_function


@BP.route('/app_keys/delete', methods=['POST'])
@jwt_required()
def app_key_delete():
    authUtils.app_key_delete(request.json)
    return jsonify("ok"), 201


@BP.route('/app_keys', methods=['POST', 'GET'])
@jwt_required()
def app_keys():
    return jsonify(authUtils.app_keys(request))


@BP.route('/verify')
@jwt_required()
def verify():
    return jsonify(authUtils.verify(request))


# ------------------------- Types ---------------------------
@BP.route('/types_select', methods=['GET'])
@jwt_required()
def get_types_ceategorie():
    return jsonify(typesUtils.get_types_categorie())


@BP.route('/types', methods=['GET'])
@jwt_required()
def types():
    return jsonify(typesUtils.get_types())


@BP.route('/types', methods=['post'])
@jwt_required()
def types_store_update():
    typesUtils.store_update(request.json)
    return jsonify("ok")


@BP.route('/types/delete', methods=['POST'])
@jwt_required()
def types_delete():
    typesUtils.delete(request.json)
    return jsonify("ok")


# ------------------------ Keywords ------------------------
@BP.route('/keywords', methods=['GET'])
@jwt_required()
def keywords():
    return jsonify(keywordsUtils.get_keywords(request.args))


@BP.route('/keywords', methods=['POST'])
@jwt_required()
def keywords_store_update():
    keywordsUtils.store_update(request.json)
    return jsonify("ok")


@BP.route('/keywords/delete', methods=['POST'])
@jwt_required()
def keywords_delete():
    keywordsUtils.delete(request.json)
    return jsonify("ok")


# ------------------------ OCR ------------------------
@BP.route('/get_ocr', methods=['POST'])
@jwt_required()
def get_ocr():
    return jsonify(Utils.ocr(base_64=Utils.upload_file_and_get_base64(request)))


@BP.route('/ocr', methods=['POST'])
@app_auth_required
def app_ocr():
    return jsonify(Utils.ocr(base_64=request.json['base_64']))


# ------------------------ Classification ------------------------
@BP.route('/get_classify', methods=['POST'])
@jwt_required()
def get_classify():
    return jsonify(classificationUtils.classify(base_64=Utils.upload_file_and_get_base64(request)))


@BP.route('/classify', methods=['POST'])
@app_auth_required
def app_classify():
    return jsonify(classificationUtils.classify(base_64=request.json['base_64']))


app.register_blueprint(BP, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=cnf.DEBUG, host='0.0.0.0', port=5000)
