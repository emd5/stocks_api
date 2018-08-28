import os
import sys
import transaction

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from pyramid.scripts.common import parse_vars

from ..models.meta import Base
from ..models import (
    get_engine,
    get_session_factory,
    get_tm_session,
    )

from ..models import MyModel
from ..models import Stock
from ..models import Portfolio
from ..models import Company


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)

    #  Creates a connection (engine) to the DB
    engine = get_engine(settings)
    #  Creates tables for out models in the DB
    Base.metadata.create_all(engine)

    #  Below is used for seeding the DB
    # session_factory = get_session_factory(engine)
    #
    # with transaction.manager:
    #     dbsession = get_tm_session(session_factory, transaction.manager)
    #
    #     # Creates an in-memory instance
    #     model = MyModel(name='one', value=1)
    #     #  The transaction to the DB
    #     dbsession.add(model)
