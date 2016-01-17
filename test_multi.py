#!/home/halverso/anaconda/bin/python
#PBS -q verylongq
#PBS -l walltime=192:00:00
#PBS -l select=20:ncpus=12
#PBS -o /nobackup0/omega/halverso/test_sched/trunk/test_output/pbs_stdout.out
#PBS -e /nobackup0/omega/halverso/test_sched/trunk/test_output/pbs_stderr.out
#PBS -V

import os
from time import sleep
from datetime import datetime
import multiprocessing

def create_file(filename):
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

if __name__ == '__main__':
    processes = {}

    for i in range(10):
        filename = '/nobackup0/omega/halverso/test_sched/trunk/test_output/%d.txt' % i
        processes[i] = multiprocessing.Process(target=create_file, args=(filename,))
        processes[i].start()

