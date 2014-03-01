#!/usr/bin/python

__author__ = 'yiqingj'

import os
import sys
import json

usage = 'delta-gen.py [config-file]'


def ingest_state(file_path):
    print file_path
    hnd_file = open( os.path.join(file_path, 'state.txt'), 'r')
    file_data = hnd_file.read()
    hnd_file.close()

    arr_lines = file_data.split("\n")
    for aLine in arr_lines:
        arr_comp = aLine.split( '=' )
        if len( arr_comp ) < 2:
            continue
        print arr_comp
        if arr_comp[0] == "sequenceNumber":
            sequence = int(arr_comp[1].strip())
            return sequence


def create_path(file_path, sequence, postfix):
    m = sequence / 1000000
    k = (sequence - (m * 1000000)) / 1000
    u = sequence - (m * 1000000) - (k * 1000)
    path = os.path.join(file_path, "%03d" % m, "%03d" % k)
    if not os.path.exists(path):
        os.makedirs(path)
    return os.path.join(path, "%03d.%s" % (u, postfix))


def create_command(working_dic='.'):
    if len(sys.argv) < 2:
        print usage
        print 'Using default config file: area-list.json'
        file_name = 'area-list.json'
    else:
        file_name = sys.argv[1]
    file = open(file_name, 'r')
    sequence = ingest_state(working_dic) -1 # assume files are in same path

    config = json.load(file)
    count = len(config)
    command_str = '../../bin/osmosis --rri workingDirectory=. --simc --tc %d' % count
    print "Number of area", count
    for area in config:
        top_left = area["bound"]["top-left"].split(",")
        bottom_right = area["bound"]["bottom-right"].split(",")
        output_name = create_path(area['folder'], sequence, 'osc.gz')

        filter_cmd = ' --bounding-box-change top=%s left=%s bottom=%s right=%s --wxc %s' \
                     % (top_left[0], top_left[1], bottom_right[0], bottom_right[1], output_name)
        command_str += filter_cmd
        if not os.path.exists(area['folder']):
            os.makedirs(area['folder'])
            if not os.path.exists(area['folder']+'/replicate.lock'):
                open(area['folder']+'/replicate.lock', 'a').close()
    return command_str

if __name__ == "__main__":
    command = create_command()
    print command
    os.system(command)





