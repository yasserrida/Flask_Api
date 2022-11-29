from src.database.models.types import Types


def get_types():
    return Types.where('select_order', '>', '0').order_by('select_order', 'ASC').get().serialize()


def store_update(payload):
    if ('id' in payload and payload['id']):
        Types.find(payload['id']).update(name=payload['name'],
                                         rule=payload['rule'],
                                         select_order=payload['select_order'],
                                         )
    else:
        Types.create(name=payload['name'],
                     rule=payload['rule'],
                     select_order=payload['select_order'],
                     )


def delete(payload):
    if (payload['id']):
        Types.find(payload['id']).delete()


def get_types_categorie():
    return Types.order_by('select_order', 'ASC').get().serialize()

