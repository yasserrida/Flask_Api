from orator import Model


class ApiCredential(Model):
    __table__ = 'api_credentials'
    __fillable__ = ['app_key', 'app_secret', 'title']

    pass
