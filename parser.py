import pyparsing as pp
from fofTypes import *

def unary_handler(s, l, t):
    return UnaryOperand(t[0][0], t[0][1])

def binary_handler(s, l, t):
    return BinaryOperand(t[0][1], t[0][0], t[0][2])

def quantor_handler(s, l, t):
    variables = list(t[0][1])
    return Quantor(t[0][0], variables, t[0][2])

def function_handler(s, l, t):
    name = t[0]
    try:
            args = list(t[1])
    except IndexError:
            args = []

    return Function(name, args)

def relation_handler(s, l, t):

    if len(t) == 3 and t[1] == "=":
        return Relation("=",t[0::2])
    else:
        name = t[0]
        try:
                args = list(t[1])
        except IndexError:
                args = []

        return Relation(name, args)

def var_handler(s, l, t):
    return Variable(t[0])


fof_const_alphabet = "abcdefghijklmnopqrstuvwxzy"
fof_variable_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXZY"

fof_const_name = pp.Word(fof_const_alphabet)
fof_var_name = pp.Word(fof_variable_alphabet)
fof_var_name.addParseAction(var_handler)

def fof_arg_list(x):
    return pp.Group(pp.Suppress("(") + pp.delimitedList( x ) + pp.Suppress(")"))

fof_function = pp.Forward()

fof_term = fof_var_name | fof_function

fof_function <<  fof_const_name + pp.Optional( fof_arg_list(fof_term) )
fof_function.addParseAction(function_handler)

fof_relation = (fof_const_name + pp.Optional( fof_arg_list( fof_term ) )) | (( fof_term ) + "=" + ( fof_term ))
fof_relation.addParseAction(relation_handler)

fof_impl_ops = pp.oneOf("=> <= <=> <~>")
fof_and_ops = pp.oneOf("& ~&")
fof_or_ops = pp.oneOf("| ~|")
fof_quantors = pp.oneOf("? !") + Group(pp.Suppress("[") + pp.delimitedList(fof_var_name) + pp.Suppress("]"))  + pp.Suppress(":")

fof_expr = operatorPrecedence( fof_relation,[
        ( "~",           1, pp.opAssoc.RIGHT, unary_handler)
    ,   ( fof_quantors,  1, pp.opAssoc.RIGHT, quantor_handler)
    ,   ( fof_or_ops,    2, pp.opAssoc.LEFT, binary_handler)
    ,   ( fof_and_ops,   2, pp.opAssoc.LEFT, binary_handler)
    ,   ( fof_impl_ops,  2, pp.opAssoc.LEFT, binary_handler)
])

komma = Suppress(",")
dot = Suppress(".")

tptp = OneOrMore(
        Group(pp.oneOf("fof") + Suppress("(") +
            Word(alphanums) + komma  +
           pp.oneOf("axiom theorem") + komma +
            fof_expr + Suppress(")") +  dot))


def parse_string(string):
    result = tptp.parseString(string)
    return list(map(lambda aList: { "type" : aList[0], "name": aList[1], "type": aList[2], "formula": aList[3] }, result))
def parse_file(filename):
    with open(filename) as f:
        return (parse_string(f.read()))
