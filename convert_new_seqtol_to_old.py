#!/usr/bin/python

__author__ = "Kyle Barlow"
__email__ = "kb@kylebarlow.com"

# Script to convert sequence tolerance generations and entities files output
# by newer versions of Rosetta into the same file format used by Colin's R
# scripts when he originally published the method

# Usage: Takes a single argument: directory containing sequence tolerance output
#  Output .entities.gz and .generations.gz files can be in any subdirectory of
#  the passed in directory argument - the script WILL find them

### WARNING: the script also overwrites these files in place, so you probably
### should make a backup first

import os
import gzip
from subprocess import Popen, PIPE, check_call
import sys
import library
import time
import re
from multiprocessing import Pool
import multiprocessing

def main():
    search_dir = sys.argv[1]
    assert(os.path.isdir(search_dir))
    
    files_to_convert = []
    for directory_root, directory, filenames in os.walk(search_dir):
        for filename in filenames:
            full_filename = os.path.join(directory_root,filename)
            if full_filename.endswith('.entities.gz'):
                files_to_convert.append(full_filename)


            if full_filename.endswith('.generations.gz'):
                files_to_convert.append(full_filename)

    print 'Found %d files to convert' % len(files_to_convert)

    r = library.Reporter('converting files')
    r.set_total_count(len(files_to_convert))
    pool = Pool()
    for f in files_to_convert:
        pool.apply_async(convert_file, args=(f,), callback=r.increment_report_callback)

    pool.close()
    pool.join()
    r.done()

def convert_file(filename):
    f = library.LineReader(filename)
    new_lines = []
    for line in f.readlines():
        data = line.strip().split()
        new_data = list(data)
        for i, datum in enumerate(data):
            if datum.startswith('AA:'):
                m = re.match('(?:AA[:])(\d+)(?:[:])([A-Z])', datum)
                assert(m)
                assert(m.group(2) in library.three_letter_codes)
                new_datum = '%d.%s' % (int(m.group(1)),
                                       library.three_letter_codes[m.group(2)])
                new_data.insert(i, new_datum)
                assert(new_data.pop(i+1)==datum)
        new_line = ''
        for i, datum in enumerate(new_data):
            if datum == 'fitness':
                new_line += ' fitness'
            else:
                new_line += datum
            if i < len(new_data)-1:
                new_line += ' '
            else:
                new_line += '\n'
        new_lines.append(new_line)

    f.close()

    os.remove(filename)
    if filename.endswith('.gz'):
        f_out = gzip.open(filename, 'wb')
        for line in new_lines:
            f_out.write(line)
            f.close()
    else:
        raise Exception('Non-zipped output not yet implemented')

if __name__ == '__main__':
    main()
