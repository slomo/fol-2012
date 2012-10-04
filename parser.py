from pyparsing import OneOrMore, Group, Suppress, oneOf, Word, opAssoc, operatorPrecedence, alphanums
from fofTypes import *

fof_binary_symbols = [ "|", "&", "=>", "<=", "~&", "~|", "<=>", "<~>" ]
fof_lambda = ( lambda s,l,t: BinaryOperand(t[0][1],t[0][0],t[0][2]) )
#def bla(s, l, t):
#
#    print(s,type(s))
#    print(l,type(l))
#    print(t[0],type(t[0]))
#    print("------------")
#    return fof_lambda(s,l,t)

fof_binary_operators = [ (op, 2, opAssoc.LEFT, fof_lambda ) for op in fof_binary_symbols ]


fof_operand = Word("abcdefghijklmnopqrstuvwxzy").setParseAction(Identifier) | oneOf("true false")
fof_expr = operatorPrecedence( fof_operand,
        [ ("~",  1, opAssoc.RIGHT, lambda s,l,t: UnaryOperand(s,t[1])) ] + fof_binary_operators )

komma = Suppress(",")
dot = Suppress(".")

tptp = OneOrMore(
        Group( oneOf("fof") + Suppress("(") +
            Word(alphanums) + komma  +
            oneOf("axiom theorem") + komma +
            fof_expr + Suppress(")") + dot))

def parse_string(string):
    return tptp.parseString(string)

def parse_file(filename):
    with open(filename) as f:
        return (parse_string(f.read()))
