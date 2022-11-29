from src.database.models.apiCredential import ApiCredential
from src.database.models.user import User
from flask_jwt import current_identity
import secrets
import bcrypt


def app_key_delete(payload):
    if (payload['id']): ApiCredential.find(payload['id']).delete()


def app_keys(request):
    if request.method == 'POST':
        result = User.find(current_identity.id).apiCredentials().create(app_key=secrets.token_urlsafe(16), app_secret=secrets.token_urlsafe(36), title=request.json['title'])
        return result.serialize()
    else:
        return User.find(current_identity.id).apiCredentials.serialize()


def app_auth_required(request):
    return ApiCredential.where('app_key', request.headers['KEY']).where('app_secret', request.headers['SECRET']).where('is_valide', "1").first()


def authenticate(username, password):
    user = User.where('email', username).first()
    return user if (user and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8'))) else None


def identity(payload):
    return User.find(payload['identity'])


def verify(request):
    user = current_identity.serialize()
    user['access_token'] = request.headers['Authorization'].split()[1]
    return user
