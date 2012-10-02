from pyparsing import *
from types import *

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

print(tptp.parseString("fof(axiom1, axiom, ~ sr & tr | x)."))
