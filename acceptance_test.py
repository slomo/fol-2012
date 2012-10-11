import resolution as r
import unittest
import operations as o
import parser as p
from fofTypes import *

def proof(fstr):

    fstr = "fof(ax,axiom, (" + fstr + ") )."
    print("fof",fstr)
    formula = p.parse_string(fstr)[0]['formula']
    formula = o.transform(formula.negate())
    return r.proof(formula)

class ResolutionTest(unittest.TestCase):

    def test_church(self):
        s = "? [X] : ! [Y] : ( big_f(X) <=> big_f(Y) )"
        s = "! [X] : big_f(X) => (" + s + ")"
        self.assertTrue(proof(s))

    def test_church_2(self):
        s = "? [X] : ! [Y] : big(X,Y)"
        self.assertTrue(not proof(s))

#   def test_church_3(self):

#       s = """( ? [Z,X] :
#     ! [Y1,Y2] :
#       ( ( ~ big_f(X,Z)
#        => big_f(Z,Y1) )
#      => ( big_f(Y2,Z)
#        => big_f(Z,Y2) ) ) )"""
#       self.assertTrue(not proof(s))

if __name__ == '__main__':
    unittest.main()

