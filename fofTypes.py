from pyparsing import *

class Formula(object):

    def negate(self):
        return UnaryOperand("~", self)

    def __eq__(self,other):
        return repr(self) == repr(other)

class Term(Formula):
    pass

class UnaryOperand(Formula):
# Since we only have 1 unary operation we can safely assume it is a negation
    def __init__(self, op, term):
        # if len(terms) > 1 something went wrong
        self.term = term
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

class BinaryOperand(Formula):

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

class Quantor(Formula):

    def __init__(self, op, list_of_vars, term):
        self.op = op
        self.variables = frozenset(list_of_vars)
        self.term = term

    def __repr__(self):
        return self.op + repr(list(self.variables)) + ":" + repr(self.term)

    def __iter__(self):
        return iter([self.term])

    def __hash__(self):
        return hash(self.op) ^ hash(self.term) ^ hash(self.variables)

class Relation(Formula):

    def __init__(self,name,terms):
        """ terms is a list of terms.
        Like in lecture, containing constants,
        variables and other terms """
        self.name = name
        self.terms = terms

    def __repr__(self):

        if len(self.terms) == 0:
            return self.name

        else:
            return self.name + "(" + ",".join(map(repr,self.terms)) + ")"

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

    __repr__ = Relation.__repr__

    def __eq__(self,other):
        return repr(self) == repr(other)

    def __iter__(self):
        return iter(self.terms)


class Variable(Term):

    def __init__(self, string):
        self.name = string

    def __repr__(self):
        return self.name

    def __hash__(self):
        return hash(self.name)

    def __eq__(self,other):
        return repr(self) == repr(other)

