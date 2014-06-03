# -*- coding: utf-8 -*-

import pyramid.threadlocal

from fas.models import provider as provider

from math import ceil


def get_config(configname):
    """ Retrieve config from configuration file.

    :arg configname: string, configuration key to look for
    :return: value of requested configuration.
    """
    registry = pyramid.threadlocal.get_current_registry()
    settings = registry.settings

    return settings[configname]


def compute_list_pages_from(str_obj, limit=50):
    """ Compute list's pages from given object.

    :arg obj: string, object to compute pages from.
    :arg limit: integer, limt object to compute pages from.
    :return: integer of nb pages.
    """
    count = getattr(provider, 'get_%s_count' % str_obj)
    count = count()

    return (int(ceil(float(count) / float(limit))), int(count))