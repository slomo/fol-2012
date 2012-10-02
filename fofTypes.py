from pyparsing import *

class UnaryOperand(object):

    def __init__(self, op, term_list):
        [op, term] = term_list[0]
        self.term = term
        self.op = op

    def __repr__(self):
        return "(" + self.op + " " + repr(self.term) + ")"

class BinaryOperand(object):

    def __init__(self, op, term_list):
        [left_term, op, right_term] = term_list[0]
        self.terms = left_term, right_term
        self.op = op

    def __repr__(self):
        return "(" + repr(self.terms[0]) + " " + self.op + " " + repr(self.terms[1]) + ")"

class Identifier(object):

    def __init__(self, string):
        self.name = string[0]

    def __repr__(self):
        return "<" + self.name + ">"
