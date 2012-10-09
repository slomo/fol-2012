#!/usr/bin/env python3
import parser as tptp
import argparse as a
import operations as o
import resolution as r
import fofTypes as f

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
        string = "fof(ax, axiom, ?[X]: r(f(a,X),Y,x) )."
        print("Input was:", string)
        x = from_string(string)

    tree = x[0]["formula"]
    print(tree)
    tree = f.UnaryOperand("~",tree)
    print("and transformed ...")
    tree = o.transform(tree)
    tree = o.transform(tree)
    print(tree)
    print("and solved")
    print(r.proof(tree))
