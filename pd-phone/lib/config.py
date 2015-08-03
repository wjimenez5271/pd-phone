import ConfigParser
import os
from sys import argv
from sys import exit


def get_config():
    config = ConfigParser.ConfigParser()
    config.read([argv[1], os.path.join(os.path.expanduser("~"), '.pd-phone.ini')])

    cfg = {}
    try:
        cfg['pd_api_key'] = config.get('main', 'pd_api_key')
        cfg['pd_subdomain'] = config.get('main', 'pd_subdomain')
    except ConfigParser.ParsingError:
        print 'Error reading config from file'
        exit(1)

    return cfg
