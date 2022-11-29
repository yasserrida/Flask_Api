from orator import Model
from orator.orm import has_many
from src.database.models.apiCredential import ApiCredential


class User(Model):
    __table__ = 'users'
    __fillable__ = ['name', 'email', 'password']
    
    @has_many
    def apiCredentials(self):
        return ApiCredential
    pass
