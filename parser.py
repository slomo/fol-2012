from pyparsing import OneOrMore, Group, Suppress, oneOf, Word, opAssoc, operatorPrecedence, alphanums
from fofTypes import *

fof_binary_symbols = [ "|", "&", "=>", "<=", "~&", "~|", "<=>", "<~>" ]
def handler(s, l, t):

    #print("s",s,type(s))
    #print("l",l,type(l))
    #print("t",t,type(t))
    #print("t0",t[0],type(t[0]))
    #print("------------")
    obj = None
    try:
        if len(t[0]) == 3:
            obj = BinaryOperand(t[0][1], t[0][0], t[0][2])
        elif len(t[0]) == 2:
            obj = UnaryOperand(t[0][0], t[0][1])
    except Exception as e:
        print("öööö",e)
    #print("t_new",t,type(t[0][0]))
    #print("############")
    return obj

fof_operand = Word("abcdefghijklmnopqrstuvwxzy").setParseAction(Identifier) | oneOf("true false")
#fof_expr = operatorPrecedence( fof_operand,
#        [ ("~",  1, opAssoc.RIGHT, lambda s,l,t: UnaryOperand(s,t[1])) ] + fof_binary_operators )

fof_expr = operatorPrecedence( fof_operand,[
        ("~",   1, opAssoc.RIGHT, handler)
    ,   ("|",   2, opAssoc.LEFT, handler)
    ,   ("&",   2, opAssoc.LEFT, handler)
    ,   ("=>",  2, opAssoc.LEFT, handler)
#    ,   ("<=",  2, opAssoc.LEFT, handler)
#    ,   ("~&",  2, opAssoc.LEFT, handler)
#    ,   ("~|",  2, opAssoc.LEFT, handler)
#    ,   ("<=>", 2, opAssoc.LEFT, handler)
#    ,   ("<~>", 2, opAssoc.LEFT, handler)
])

komma = Suppress(",")
dot = Suppress(".")

tptp = OneOrMore(
        Group( oneOf("fof") + Suppress("(") +
            Word(alphanums) + komma  +
            oneOf("axiom theorem") + komma +
            fof_expr + Suppress(")") +  dot))


def parse_string(string):
    print("res", tptp.parseString(string))
    return tptp.parseString(string)

def parse_file(filename):
    with open(filename) as f:
        return (parse_string(f.read()))
