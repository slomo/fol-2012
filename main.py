#!/usr/bin/env python3
import parser as tptp
import argparse as a
import operations as o

def from_file(file):
    return tptp.parse_file(file)

def from_string(string):
    return tptp.parse_string(string)

if __name__ == '__main__':

    parser = a.ArgumentParser(description='A simple fof solver using tptp syntax')
    parser.add_argument('--file', action='store')
    args = vars(parser.parse_args())
    x = 0
    if args['file']:
        x = from_file(args['file'])
        import pdb; pdb.set_trace()
        print(x)
    else :
        x = from_string("fof(axiom1, axiom, b <~> c).")

    tree = x[0][3]
    print(tree)
    o.transform(tree)
    print("and transformed ...")
    print(tree)
