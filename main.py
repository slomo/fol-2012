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
        fof_data = from_string("fof(ax,axiom," + args['formula'] + ").")
    else :
        string = "fof(ax, axiom, ![X]: r(X) => ?[Y]:r(Y) )."
        fof_data = from_string(string)
    import pprint
    pprint.pprint(fof_data)
    org_formula = fof_data[0]["formula"]
    print("input formula:",org_formula)
    formula = org_formula.negate()
    formula = o.transform(formula)
    print("transform negated formula:", formula)
    result = r.proof(formula)

    if result:
        print("formula is theorem")
    else:
        formula = o.transform(org_formula)
        if r.proof(formula):
            print("formula is counter theorem")
        else:
            print("Unable")

