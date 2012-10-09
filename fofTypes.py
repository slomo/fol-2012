from pyparsing import *

class Formula(object):

    def negate(self):
        return UnaryOperand("~", self)

class Term(Formula):
    pass

class UnaryOperator(Formula):
# Since we only have 1 unary operation we can safely assume it is a negation
    def __init__(self, op, terms):
        # if len(terms) > 1 something went wrong
        if len(terms) > 1: raise Exception('Too many arguments for unary operator', ' ')
        self.terms = terms
        self.op = op

    def __repr__(self):
        return self.op + repr(self.term)

    def __eq__(self,other):
        return repr(self) == repr(other)

    def __hash__(self):
        return hash(self.op) ^ hash(self.term)

    def negate(self):
        return self.term

    def __iter__(self):
        return iter([self.term])

class BinaryOperator(Formula):

    def __init__(self, op, left_term, right_term):
        self.terms = (left_term, right_term)
        self.op = op

    def __repr__(self):
        return "(" + repr(self.terms[0]) + " " + self.op + " " + repr(self.terms[1]) + ")"
    def __eq__(self,other):
        return repr(self) == repr(other)

    def __hash__(self):
        return hash(self.op) ^ hash(self.terms)

    def __iter__(self):
        return iter(self.terms)

class Relation(Formula):

    def __init__(self,name,terms):
        """ terms is a list of terms.
        Like in lecture, containing constants,
        variables and other terms """
        self.name = name
        self.terms = terms

    # FIXME:
    def __repr__(self):
        termlist = repr(self.terms[0])
        for x in range(len(self.terms)):
            if x != 0:
                termlist = termlist + ", " + repr(self.terms[x])
        return self.name + "(" + termlist + " ) "

    def __eq__(self,other):
        return repr(self) == repr(other)

    def __iter__(self):
        return iter(self.terms)

class Function(Term):

    def __init__(self,name,terms):
        """ terms is a list of terms.
        Like in lecture, containing constants,
        variables and other terms """
        self.name = name
        self.terms = terms

    def __repr__(self):
        return self.name + "(" + repr(self.terms) + " ) "

    def __eq__(self,other):
        return repr(self) == repr(other)

    def __iter__(self):
        return iter(self.terms)


class Variable(Term):

    def __init__(self, string):
        self.name = string

    def __repr__(self):
        return self.name

    def __eq__(self,other):
        return repr(self) == repr(other)

