import resolution as r
import unittest
import operations as o
from fofTypes import *

def proof(formula):
    formula = o.transform(formula.negate())
    return r.proof(formula)

for_all = lambda v,x:  Quantor("!", [ v ], x )

class ResolutionTest(unittest.TestCase):

    def test_invalid_prop(self):
        formula = BinaryOperator("&",
                BinaryOperator("&",Relation("a"),Relation("b")),
                UnaryOperator("~", Relation("a")))
        self.assertTrue(not proof(formula))

    def test_simple_prop(self):
        formula = BinaryOperator("|", Relation("a"), UnaryOperator("~",Relation("a")))
        self.assertTrue(proof(formula))

    def test_simple_quantor(self):
        qf =  Quantor("!", [Variable("X")], Relation("r",[Variable("X")]))
        f = BinaryOperator("=>",qf,Relation("r",[Function("a")]))
        self.assertTrue(proof(f))

    def test_multi_var_quantor(self):
        qf =  Quantor("!", [Variable("X"), Variable("Y")], Relation("r",[Variable("Y"), Variable("X")]))
        f = BinaryOperator("=>",qf,Relation("r",[Function("a"), Function("a")]))
        self.assertTrue(proof(f))

    def test_nested_quantor(self):
        x = Variable("X")
        y = Variable("Y")
        q = for_all(x,Relation("r",[x,y]))
        q = for_all(y,q)

        f = BinaryOperator("=>",q,Relation("r",[Function("a"), Function("b")]))
        self.assertTrue(proof(f))

    def test_slide_17(self):
        x = Variable("X")
        y = Variable("Y")

        t = BinaryOperator('|', Relation('p',[x]), Relation('q',[x]))
        q1 = for_all(x,t)

        q2 = Quantor('?',[x],Relation('p',[x]))
        q3 = for_all(x, Relation('q',[x]))

        f = BinaryOperator("=>", q1, BinaryOperator("|", q2, q3))
        self.assertTrue(proof(f))

if __name__ == '__main__':
    unittest.main()

