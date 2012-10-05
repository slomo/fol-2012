from pyparsing import *
import pyparsing as pp
from fofTypes import *


fof_const_alphabet = "abcdefghijklmnopqrstuvwxzy"
fof_variable_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXZY"

def unary_handler(s, l, t):
    return UnaryOperand(t[0][0], t[0][1])

def binary_handler(s, l, t):
    return BinaryOperand(t[0][1], t[0][0], t[0][2])

def quantor_handler(s, l, t):
    variables = list(map(Variable, t[0][1]))
    return Quantor(t[0][0], variables, t[0][2])

fof_operand = Word(fof_const_alphabet).setParseAction(Identifier) | oneOf("true false")


fof_impl_ops = oneOf("=> <= <=> <~>")
fof_and_ops = oneOf("& ~&")
fof_or_ops = oneOf("| ~|")
fof_quantors = oneOf("? !") + Group(pp.Suppress("[") + pp.delimitedList(Word(fof_variable_alphabet)) + pp.Suppress("]"))  + pp.Suppress(":")

fof_expr = operatorPrecedence( fof_operand,[
        ( "~",           1, opAssoc.RIGHT, unary_handler)
    ,   ( fof_quantors,  1, opAssoc.RIGHT, quantor_handler)
    ,   ( fof_or_ops,    2, opAssoc.LEFT, binary_handler)
    ,   ( fof_and_ops,   2, opAssoc.LEFT, binary_handler)
    ,   ( fof_impl_ops,  2, opAssoc.LEFT, binary_handler)
])

komma = Suppress(",")
dot = Suppress(".")

tptp = OneOrMore(
        Group( oneOf("fof") + Suppress("(") +
            Word(alphanums) + komma  +
            oneOf("axiom theorem") + komma +
            fof_expr + Suppress(")") +  dot))


def parse_string(string):
    result = tptp.parseString(string)
    return list(map(lambda aList: { "type" : aList[0], "name": aList[1], "type": aList[2], "formula": aList[3] }, result))
def parse_file(filename):
    with open(filename) as f:
        return (parse_string(f.read()))
