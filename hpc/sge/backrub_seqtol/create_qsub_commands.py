#!/usr/bin/env python2

# The MIT License (MIT)
#
# Copyright (c) 2015 Shane O'Connor
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

'''
This script creates command lines which can be used to run the benchmark on an linux-based SGE submission host.

  Usage:     python create_qsub_commands.py BENCHMARK_PATH
      or     python create_qsub_commands.py BENCHMARK_PATH test_mode

Written by Shane O'Connor 2015.
'''

import sys
import os

def print_usage():
    print('\tUsage:     python %s BENCHMARK_PATH' % __file__)
    print('\t    or     python %s BENCHMARK_PATH test_mode\n' % __file__)

if __name__ == '__main__':
    if not(2 <= len(sys.argv) <= 3):
        print('\nThis script expects to be passed the path to this benchmark capture (the directory containing the analysis, data, hpc, etc. directories).\n')
        print_usage()
        sys.exit(1)

    test_mode = ''
    if len(sys.argv) == 3:
        if sys.argv[2] != 'test_mode':
            print('\nError: Expected "test_mode" as the third argument.\n')
            print_usage()
            sys.exit(2)
        test_mode = ' test_mode'

    bpath = os.path.abspath(os.path.normpath(sys.argv[1]))
    if not os.path.exists(bpath):
        print("\nError: The path %s could not be found. Printing the command lines anyway.\n" % bpath)

    print('\n' + '*' * 3 + ' Commands for running the benchmark ' + '*' * 3 + '\n')
    qsub_lines = [l.strip() for l in open('README.rst').read().split('\n') if l.strip().startswith('qsub')]
    for qsub_line in qsub_lines:
        idx = qsub_line.find('-N bs_')
        pdb_id = qsub_line[idx+6:].split()[0]
        print('mkdir %s' % pdb_id)
        print('cd %s' % pdb_id)
        print(qsub_line.replace('${BENCHMARK_PATH}', bpath) + test_mode)
        print('cd ..\n')



