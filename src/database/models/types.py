from orator import Model


class Types(Model):
    __table__ = 'types'
    __fillable__ = ['name', 'rule', 'select_order', 'depends_on', 'category_order', 'required_type', 'ruleToExclude']

    pass
