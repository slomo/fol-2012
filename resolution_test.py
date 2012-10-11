import resolution as r
import unittest
import operations as o
from fofTypes import *

def proof(formula):
    formula = o.transform(formula.negate())
    return r.proof(formula)

class ResolutionTest(unittest.TestCase):

    #def test_more(self):
    #    formula = BinaryOperator("&",
    #        BinaryOperator("&",Relation("a"),Relation("b")),
    #        UnaryOperator("~", Relation("a")))
    #    self.assertTrue(proof(formula))

    def test_a_or_not_a(self):
        formula = BinaryOperator("|", Relation("a"), UnaryOperator("~",Relation("a")))
        self.assertTrue(proof(formula))

    def test_simple_quantor(self):
        qf =  Quantor("!", [Variable("X")], Relation("r",[Variable("X")]))
        f = BinaryOperator("=>",qf,Relation("r",[Function("a")]))
        self.assertTrue(proof(f))

    def test_double_quantor(self):
        qf =  Quantor("!", [Variable("X"), Variable("Y")], Relation("r",[Variable("Y"), Variable("X")]))
        f = BinaryOperator("=>",qf,Relation("r",[Function("a"), Function("a")]))
        self.assertTrue(proof(f))

if __name__ == '__main__':
    unittest.main()

