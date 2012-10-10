#!/usr/bin/env python3
import parser as tptp
import argparse as a
import operations as o
import resolution as r
import fofTypes as f
import unification as u

def from_file(file):
    return tptp.parse_file(file)

def from_string(string):
    return tptp.parse_string(string)

if __name__ == '__main__':

    parser = a.ArgumentParser(description='A simple fof solver using tptp syntax')
    parser.add_argument('--file', action='store')
    parser.add_argument('--formula', action='store')

    args = vars(parser.parse_args())
    if args['file']:
        fof_data = from_file(args['file'])
    elif args['formula']:
        fof_data = from_string(args['formula'])
    else :
        string = "fof(ax, axiom, ?[X]: r(f(a,X),Y,x) )."
        fof_data = from_string(string)

    for x in fof_data:
	    formula = x["formula"]
	    print("input formula:",formula)
	    formula = formula.negate()
	    formula = o.transform(formula)
	    print("transform negated formula:", formula)
	    result = r.proof(formula)
	    print("formula holds:", result)
