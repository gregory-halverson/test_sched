#!/home/halverso/anaconda/bin/python
#PBS -q verylongq
#PBS -l walltime=192:00:00
#PBS -l select=1:ncpus=1
#PBS -o /nobackup0/omega/halverso/test_sched/trunk/test_output/pbs_stdout.out
#PBS -e /nobackup0/omega/halverso/test_sched/trunk/test_output/pbs_stderr.out
#PBS -V

import os

print('PBS_NODEFILE: ' + os.getenv('PBS_NODEFILE'))
