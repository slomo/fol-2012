from pyparsing import *

class UnaryOperand(object):
# Since we only have 1 unary operation we can safely assume it is a negation
    def __init__(self, op, term):
        self.term = term
        self.op = op

    def __repr__(self):
        return "(" + self.op + " " + repr(self.term) + ")"

    def __eq__(self,other):
        return repr(self) == repr(other)

    def __hash__(self):
        return hash(self.op) ^ hash(self.term)

class BinaryOperand(object):

    def __init__(self, op, left_term, right_term):
        self.terms = (left_term, right_term)
        self.op = op

    def __repr__(self):
        return "(" + repr(self.terms[0]) + " " + self.op + " " + repr(self.terms[1]) + ")"
    def __eq__(self,other):
        return repr(self) == repr(other)

    def __hash__(self):
        return hash(self.op) ^ hash(self.terms)

class Identifier(object):

    def __init__(self, string):
        self.name = string[0]

    def __repr__(self):
        return "<" + self.name + ">"

    def __eq__(self,other):
        return repr(self) == repr(other)

    def __hash__(self):
        return hash(self.name)

class Quantor(object):

    def __init__(self, string, variables, term):
        self.quantor = string
        self.variables = variables
        self.term = term

    def __repr__(self):
        return self.quantor + " " + repr(self.variables) + " : " + repr(self.term)

    def __eq__(self,other):
        return repr(self) == repr(other)

class Variable(object):

    def __init__(self, string):
        self.name = string

    def __repr__(self):
        return self.name

    def __eq__(self,other):
        return repr(self) == repr(other)

