from fofTypes import *
import json

def unary_handler(data):
    f = load(data['formula'])
    return UnaryOperator("~",f)

def binary_handler(data):
    left = load(data['leftFormula'])
    right = load(data['leftFormula'])
    return BinaryOperator(data['op'], left, right)

def quantor_handler(data):
    variables = [ load(x) for x in data["variables"] ]
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

def load_file(filename):

    with open(filename) as f:
        tree = json.load(f)

        for form in tree:
            form["formula"] = load(form["formula"])

        return tree
