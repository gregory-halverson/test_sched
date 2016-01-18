#!/home/halverso/anaconda/bin/python
#PBS -q shortq
#PBS -l walltime=00:10:00
#PBS -l select=20:ncpus=12
#PBS -o /nobackup0/omega/halverso/test_sched/trunk/test_output/test_pool.out
#PBS -e /nobackup0/omega/halverso/test_sched/trunk/test_output/test_pool.err
#PBS -V

import os
from time import sleep
from datetime import datetime
import multiprocessing

def create_file(directory, number):
    filename = directory + '/%d.txt' % i

    print("creating test file '%s'" % filename)

    with open(filename, 'w') as f:
        f.write(str(datetime.utcnow()))

    if os.path.exists(filename):
        print("test file '%s' successfully created" % filename)
    else:
        print("unable to create test file '%s'" % filename)

    return filename

if __name__ == '__main__':
    directory = '/nobackup0/omega/halverso/test_sched/trunk/test_output'

    args_list = [(directory, i) for i in range(100)]

    pool = multiprocessing.Pool(processes=12)

    results = pool.map(create_file, args_list)

    print('results:')
    print(results)


