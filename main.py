#!/usr/bin/env python3
import parser as tptp
import argparse as a
import operations as o
import resolution as r
import fofTypes as f
import unification as u
import loader as l

def from_file(file):
    return tptp.parse_file(file)

def from_string(string):
    return tptp.parse_string(string)

if __name__ == '__main__':

    parser = a.ArgumentParser(description='A simple fof solver using tptp syntax')
    parser.add_argument('--file', action='store')
    parser.add_argument('--jsonfile', action='store')
    parser.add_argument('--formula', action='store')

    args = vars(parser.parse_args())
    if args['file']:
        fof_data = l.parse_and_load(args['file'])
        #fof_data = from_file(args['file'])
    elif args['formula']:
        fof_data = from_string("fof(ax,axiom," + args['formula'] + ").")
    elif args['jsonfile']:
        fof_data = l.load_file(args['jsonfile'])
    else :
        string = "fof(ax, axiom, ![X]: r(X) => ?[Y]:r(Y) ).fof(ax, conjecture, ![X]: r(X) => ?[Y]:r(Y) )."
        fof_data = from_string(string)

    print("input formula:",fof_data)
    conjectures = []
    axioms = []
    for formula in fof_data:
        if formula['type'] in ('axiom', 'theorem'):
            formula = o.transform(formula['formula'])
            axioms.append(formula)
        elif formula['type'] in ('conjecture'):
            f = formula['formula'].negate()
            f = o.transform(f)
            conjectures.append(f)
    print('axioms: ', axioms)
    print('conjectures: ', conjectures)
    for conjecture in conjectures:
        print("working on: ", conjecture)
        stuff = []
        stuff.append(conjecture)
        stuff += axioms
        print(type(stuff))
        result = r.proof(stuff)
        if result:
            print("formula is theorem")
        else:
            stuff[0] = o.transform(conjecture.negate())
            if r.proof(stuff):
                print("formula is counter theorem")
            else:
                print("Unable")
