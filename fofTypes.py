from pyparsing import *

class UnaryOperand(object):
# Since we only have 1 unary operation we can safely assume it is a negation
    def __init__(self, op, term):
        self.term = term
        self.op = op

    def __repr__(self):
        return "(" + self.op + " " + repr(self.term) + ")"

class BinaryOperand(object):

    def __init__(self, op, left_term, right_term):
        self.terms = (left_term, right_term)
        self.op = op

    def __repr__(self):
        return "(" + repr(self.terms[0]) + " " + self.op + " " + repr(self.terms[1]) + ")"

class Identifier(object):

    def __init__(self, string):
        self.name = string[0]

    def __repr__(self):
        return "<" + self.name + ">"
