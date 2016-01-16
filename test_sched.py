#!/home/halverso/anaconda/bin/python
#PBS -q verylongq
#PBS -l walltime=192:00:00
#PBS -l select=1:ncpus=1
#PBS -o /nobackup0/omega/halverso/test_sched/trunk/test_output/pbs_stdout.out
#PBS -e /nobackup0/omega/halverso/test_sched/trunk/test_output/pbs_stderr.out
#PBS -V

import os
import subprocess

print('')
print('checking cluster status')

if os.getenv('PBS_ENVIRONMENT'):
    print('running in pbs environment')
    print('PBS_ENVIRONMENT: ' + os.getenv('PBS_ENVIRONMENT'))
else:
    print('not running on cluster')

print('')

print('')
print('checking PATH')
print('PATH: ' + os.getenv('PATH'))
print('')

print('')
print('checking gdal status')

try:
    import gdal
    print('able to import gdal on cluster')
except Exception, e:
    print('unable to import gdal on cluster')
    print(e)

print('')

print('')
print('checking heg status')

heg_process = subprocess.Popen('hegtool', stdout=subprocess.PIPE, stderr=subprocess.PIPE)

heg_out, heg_err = heg_process.communicate()

print('')
print(heg_err)
print('')

print('')
print('testing parallel process spawning')

processes = {}

for i in range(10):
    processes[i] = subprocess.Popen(['create_test_file.py', '/nobackup0/omega/halverso/test_sched/trunk/test_output/%d.txt' % i],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)

output = {}

for i in range(10):
    out, err = processes[i].communicate()
    output[i] = out

print(output)
print('')