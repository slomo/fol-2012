#!/usr/bin/env python3
import parser as tptp
import argparse as a
import operations as o

def from_file(file):
    return tptp.parse_file(file)

axoims = []


if __name__ == '__main__':

    parser = a.ArgumentParser(description='A simple fof solver using tptp syntax')
    parser.add_argument('--file', action='store')
    args = vars(parser.parse_args())
    if args['file']:
        x = from_file(args['file'])
        x = x[0][3]
        import pdb; pdb.set_trace()
