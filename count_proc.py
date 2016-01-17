#!/home/halverso/anaconda/bin/python
#PBS -q verylongq
#PBS -l walltime=192:00:00
#PBS -l select=20:ncpus=12
#PBS -o /nobackup0/omega/halverso/test_sched/trunk/test_output/pbs_stdout.out
#PBS -e /nobackup0/omega/halverso/test_sched/trunk/test_output/pbs_stderr.out
#PBS -V

import os
import multiprocessing

print('PBS_NODEFILE: ' + os.getenv('PBS_NODEFILE'))
print('CPUs: %d' % multiprocessing.cpu_count())
