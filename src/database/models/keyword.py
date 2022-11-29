from orator import Model


class keyword(Model):
    __table__ = 'keywords'
    __fillable__ = ['keyword', 'poid', 'type', 'isExluded']

    pass
