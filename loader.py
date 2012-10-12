from fofTypes import *
import json

def unary_handler(data):
    f = load(data['formula'])
    return UnaryOperator("~",F)

def binary_handler(data):
    left = load(data['leftFormula'])
    right = load(data['leftFormula'])
    return BinaryOperator(data['op'], left, right)

def quantor_handler(data):
    return Quantor(data["quantor"], load(data["variables"]), load(data["formula"]))

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

    print(data)
    if data.type == "relation":
        relation_handler(data)
    elif data.type == "function":
        function_handler(data)
    elif data.type == "binaryOperator":
        binary_handler(data)
    elif data.type == "unaryOperator":
        unary_handler(data)
    elif data.type == "variable":
        variable_handler(data)

def load_file(filename):

    with open(filename) as f:
        tree = json.load(f)

        for form in tree:
            form["formula"] = load(form["formula"])

        return tree
