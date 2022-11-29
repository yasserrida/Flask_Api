from src.database.models.keyword import keyword


def get_keywords(args):
    orderBy = 'types.' + args['orderBy'] if 'orderBy' in args and args['orderBy'] else 'types.select_order'
    return keyword.select('keywords.*').left_join('types', 'types.id', '=', 'keywords.type_id').order_by(orderBy).get().serialize()


def store_update(payload):
    if (payload['id']):
        keyword.find(payload['id']).update(
            keyword=payload['keyword'], poid=payload['poid'], type_id=payload['type_id'])
    else:
        keyword.create(
            keyword=payload['keyword'], poid=payload['poid'], type_id=payload['type_id'])


def delete(payload):
    if (payload['id']):
        keyword.find(payload['id']).delete()
