# This file is a part of IoT-LAB client
# Copyright (C) 2019 INRIA (Contact: admin@iot-lab.info)
# Contributor(s) : see AUTHORS file
#
# This software is governed by the CeCILL license under French law
# and abiding by the rules of distribution of free software.  You can  use,
# modify and/ or redistribute the software under the terms of the CeCILL
# license as circulated by CEA, CNRS and INRIA at the following URL
# http://www.cecill.info.
#
# As a counterpart to the access to the source code and  rights to copy,
# modify and redistribute granted by the license, users are provided only
# with a limited warranty  and the software's author,  the holder of the
# economic rights,  and the successive licensors  have only  limited
# liability.
#
# The fact that you are presently reading this means that you have had
# knowledge of the CeCILL license and that you accept its terms.

import itertools
import sys

import os


def read_file(file_path, opt=''):
    """ Open and read a file """
    with open(os.path.expanduser(file_path), 'r' + opt) as _fd:  # expand '~'
        return _fd.read()


def read_custom_api_url():
    """ Return the customized api url from:
     * config file in <HOME_DIR>/.iotlab.api-url
     * or environment variable IOTLAB_API_URL
    """
    try:
        # try getting url from config file
        api_url = read_file('~/.iotlab.api-url').strip()
    except IOError:
        # try getting url from environment variable, None if undefined
        api_url = os.getenv('IOTLAB_API_URL')

    if api_url:
        sys.stderr.write("Using custom api_url: {}\n".format(api_url))
    return api_url.rstrip('/')


def flatten_list_list(list_list):
    """Flatten given list of list.

    >>> flatten_list_list([[1, 2, 3], [4], [5], [6, 7, 8]])
    [1, 2, 3, 4, 5, 6, 7, 8]
    """
    return list(itertools.chain.from_iterable(list_list))


def _expand_minus_str(minus_nodes_str):
    """ Expand a '1-5' or '6' string to a list on integer
    :raises: ValueError on invalid values
    """
    minus_node = minus_nodes_str.split('-')
    res = None
    if len(minus_node) == 1:
        # ['6']
        res = [int(minus_node[0])]
    else:
        # ['1', '4'] or ['7', '8']
        first, last = minus_node
        nodes_range = range(int(first), int(last) + 1)
        # first >= last
        if len(nodes_range) <= 1:
            raise ValueError

        # Add nodes range
        res = nodes_range
    return res


def expand_short_nodes_list(nodes_str):
    """ Expand short nodes_list '1-5+6+8-12' to a regular nodes list

    >>> expand_short_nodes_list('1-4+6+7-8')
    [1, 2, 3, 4, 6, 7, 8]

    >>> expand_short_nodes_list('1-4-5')
    Traceback (most recent call last):
    ValueError: Invalid nodes list: 1-4-5 ([0-9+-])

    >>> expand_short_nodes_list('3-3')
    Traceback (most recent call last):
    ValueError: Invalid nodes list: 3-3 ([0-9+-])

    >>> expand_short_nodes_list('3-2')
    Traceback (most recent call last):
    ValueError: Invalid nodes list: 3-2 ([0-9+-])

    >>> expand_short_nodes_list('a-b')
    Traceback (most recent call last):
    ValueError: Invalid nodes list: a-b ([0-9+-])
    """

    try:
        # '1-4+6+8-8'
        nodes_ll = [_expand_minus_str(minus_nodes_str) for minus_nodes_str in
                    nodes_str.split('+')]
        # [[1, 2, 3], [6], [12]]
        return flatten_list_list(nodes_ll)
    except ValueError:
        # invalid: 6-3 or 6-7-8 or non int values
        raise ValueError('Invalid nodes list: %s ([0-9+-])' % nodes_str)
