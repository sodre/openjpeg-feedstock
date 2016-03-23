#!/usr/bin/env python

"""
Test script for openjpeg.

Currently main purpose is to check that the openjpeg library
if linked dynamically to libpng, libtiff and libz as in 
the latest build recipe.
"""

import subprocess

# command we run to get output - for subprocess.check_output
INSPECT_COMMAND = ['conda', 'inspect', 'linkages', 'openjpeg', '--name', '_test']

# Currently we only check that this string exists in the output
# of INSPECT_COMMAND.
# This allows some difference in the endings (versions, extension etc)
# but may need to be tightened up at some stage.
# Need to be bytes to keep Python3 happy (subprocess.check_output returns bytes)
REQ_LIBS = (b'lib/libtiff', b'lib/libpng', b'lib/libz')

data = subprocess.check_output(INSPECT_COMMAND)
for lib in REQ_LIBS:
    if lib not in data:
        raise SystemExit('Library %s not found in linkages output' % lib)

