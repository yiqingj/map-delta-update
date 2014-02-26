#!/usr/bin/python
__author__ = 'yiqingj'

import os
import sys

def replicate():
    command = '../../bin/osmosis --replicate-apidb authFile=dbAuth.txt allowIncorrectSchemaVersion=true ' \
              '--write-replication workingDirectory=data'
    os.system(command)

if __name__ == "__main__":
    replicate()