from pyparsing import OneOrMore, Group, Suppress, oneOf, Word, opAssoc, operatorPrecedence, alphanums
from fofTypes import *

fof_binary_symbols = [ "|", "&", "=>", "<=", "~&", "~|", "<=>", "<~>" ]
fof_binary_operators = [ (op, 2, opAssoc.LEFT, BinaryOperand) for op in fof_binary_symbols ]


fof_operand = Word("abcdefghijklmnopqrstuvwxzy").setParseAction(Identifier) | oneOf("true false")
fof_expr = operatorPrecedence( fof_operand,
        [ ("~",  1, opAssoc.RIGHT, UnaryOperand) ] + fof_binary_operators )

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
        parse_String(f.read())
