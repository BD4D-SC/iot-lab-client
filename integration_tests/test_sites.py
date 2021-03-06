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

from integration_tests import API

api = API.sites


def test_get_sites():
    sites = api.get_sites()
    assert sites.items
    assert all([item.site for item in sites.items])


def test_get_sites_details():
    sites = api.get_sites()
    sites_details = api.get_sites_details()
    assert sites.items
    assert sites_details.items

    sites = set(item.site for item in sites.items)
    sites_details = set(item.site for item in sites_details.items)

    assert sites == sites_details
