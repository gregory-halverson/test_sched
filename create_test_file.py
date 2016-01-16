#!/home/halverso/anaconda/bin/python

import os
import sys

if not len(sys.argv) > 1:
    print('no filename provided')
    exit()

filename = sys.argv[1]

print("creating test file '%s'" % filename)

with open(filename, 'w') as f:
    f.write('test content')

if os.path.exists(filename):
    print("test file '%s' successfully created" % filename)
else:
    print("unable to create test file '%s'" % filename)

