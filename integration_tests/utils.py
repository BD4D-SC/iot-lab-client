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
""" utils for iot-lab-client integration tests"""
import hashlib
import time
from concurrent.futures import TimeoutError


def wait_until(callable, interval=0.1, timeout=1):
    start = time.time()
    while not callable() and time.time() - start < timeout:
        time.sleep(interval)
    if time.time() - start > timeout:
        raise TimeoutError


def files_match(f1, f2):
    with open(f1, 'rb') as file1, \
            open(f2, 'rb') as file2:
        hash1 = hashlib.md5(file1.read()).hexdigest()
        hash2 = hashlib.md5(file2.read()).hexdigest()
        assert hash1 == hash2
