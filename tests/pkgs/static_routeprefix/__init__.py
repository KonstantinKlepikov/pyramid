def includeme(config):
    config.add_static_view('/static', 'tests:fixtures')
    config.include(includeme2, route_prefix='/prefix')


def includeme2(config):
    config.add_static_view('/static', 'tests:fixtures/static')
