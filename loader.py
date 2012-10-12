from fofTypes import *
from subprocess import Popen, PIPE
import json
import os

def unary_handler(data):
    f = load(data['formula'])
    return UnaryOperator("~",f)

def binary_handler(data):
    left = load(data['leftFormula'])
    right = load(data['leftFormula'])
    return BinaryOperator(data['op'], left, right)

def quantor_handler(data):
    variables = [ load(x) for x in data["variables"] ]
    print("---------------------",load(data["formula"]))
    return Quantor(data["op"], variables, load(data["formula"]))

def function_handler(data):
    name = data["name"]
    args = [ load(x) for x in data["terms"] ]
    return Function(name, args)

def relation_handler(data):
    name = data["name"]
    args = [ load(x) for x in data["terms"] ]
    return Relation(name, args)

def variable_handler(data):
    return Variable(data['name'])

def load(data):
    dtype = data["type"]
    if dtype == "relation":
        return relation_handler(data)
    elif dtype == "function":
        return function_handler(data)
    elif dtype == "binaryOperator":
        return binary_handler(data)
    elif dtype == "unaryOperator":
        return unary_handler(data)
    elif dtype == "variable":
        return variable_handler(data)
    elif dtype == "quantor":
        return quantor_handler(data)
    else:
        print(dtype)
        assert(False)

def load_tree(tree):
    for form in tree:
        form["formula"] = load(form["formula"])

    return tree

def load_file(filename):

    with open(filename) as f:
        tree = json.load(f)
        return load_tree(tree)

def parse_and_load(filename):

    parser = Popen(["./parser", filename], stdout=PIPE)

    parser.wait()
    (data,other) = parser.communicate()

    data = data.decode('utf-8')
    return load_tree(json.loads(data))
