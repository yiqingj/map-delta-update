#!/usr/bin/python

__author__ = 'yiqingj'

import os
import sys
import json

usage = 'delta-gen.py [config-file]'


def create_command():
    if len(sys.argv) != 2:
        print usage
        print 'Using default config file: area-list.json'
        file_name = 'area-list.json'
    else:
        file_name = open(sys.argv[1], 'r')
    config = json.load(file_name)
    count = len(config)
    command = '../../bin/osmosis --rri workingDirectory=. --simc --tc %d' % count
    print "Number of area", count
    for area in config:
        top_left = area["bound"]["top-left"].split(",")
        bottom_right = area["bound"]["bottom-right"].split(",")
        filter_cmd = ' --bounding-box-change top=%s left=%s bottom=%s right=%s --write-replication workingDirectory=%s' \
                     % (top_left[0], top_left[1], bottom_right[0], bottom_right[1], area['file'])
        command += filter_cmd
    print command

if __name__ == "__main__":
    create_command()




