from __future__ import absolute_import

import ConfigParser
import os

COLLABORATORS_CONFIG_FILE = os.path.join(os.path.dirname(__file__),
                                         'collaborators.ini')


def get_people_from_config(api, config_abs_path):
    config = ConfigParser.ConfigParser()
    config.read(config_abs_path)
    repo = api.owner + '/' + api.repo

    try:
        return config.items(repo)
    except ConfigParser.NoSectionError:
        return []       # No people


def get_collaborators(api):
    config_items = get_people_from_config(api, COLLABORATORS_CONFIG_FILE)
    return [username for (username, _) in config_items]


def linear_search(sequence, element, callback=lambda thing: thing):
    '''
    The 'in' operator also does a linear search over a sequence, but it checks
    for the exact match of the given object, whereas this makes use of '==',
    which calls the '__eq__' magic method, which could've been overridden in
    a custom class (which is the case for our test lint)
    '''
    for thing in sequence:
        if element == thing:    # element could have an overridden '__eq__'
            callback(thing)
