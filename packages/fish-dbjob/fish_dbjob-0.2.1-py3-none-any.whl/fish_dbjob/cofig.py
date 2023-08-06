import configparser
from os.path import expanduser, join


def get(profile):
    _home = expanduser('~')
    raw_config = configparser.RawConfigParser()
    raw_config.read(join(_home, '.databrickscfg'))

    host = raw_config.get(profile, 'host')
    token = raw_config.get(profile, 'token')

    return (host, token)
