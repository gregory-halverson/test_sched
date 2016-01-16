#!/home/halverso/anaconda/bin/python

import os
import sys
from datetime import datetime
from time import sleep

if not len(sys.argv) > 1:
    print('no filename provided')
    exit()

filename = sys.argv[1]

print("creating test file '%s'" % filename)

with open(filename, 'w') as f:
    start = datetime.utcnow()
    f.write('starting test at ' + str(start) + '\n')
    f.write('sleeping\n')
    sleep(60)
    end = datetime.utcnow()
    f.write('finished test at ' + str(end) + '\n')

if os.path.exists(filename):
    print("test file '%s' successfully created" % filename)
else:
    print("unable to create test file '%s'" % filename)

