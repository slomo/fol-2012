#!/usr/bin/env python3
import parser as tptp
import argparse as a
import operations as o
import resolution as r

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
        print(x)
    else :
        #x = from_string("(( not a and b) or q )")
        x = from_string("fof(ax, axiom, ~(( ~ a & b) | q ) ).")

    tree = x[0][3]
    print(tree)
    tree = o.transform(tree)
    print("and transformed ...")
    print(tree)
    print("and solved")
    print(r.proof(tree))
