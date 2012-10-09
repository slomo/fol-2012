import resolution as r
import unittest
import operations as o
from fofTypes import *

class ResolutionTest(unittest.TestCase):


    def test_a_or_not_a(self):

        formula = BinaryOperand("&",Identifier("a"),UnaryOperand("~",Identifier("a")))

        self.assertTrue(r.proof(formula))

    def test_more(self):

        formula = BinaryOperand("&",
			BinaryOperand("&",Identifier("a"),Identifier("b")),
			UnaryOperand("~", Identifier("a")))

        self.assertTrue(r.proof(formula))

    def test_a_or_not_a(self):
	formula = BinaryOperand("|", Identifier("a"), UnaryOperand("~",Identifier("a")))
	formula = self.negate_and_transform(formula)
	self.assertTrue(r.proof(formula))

    def negate_and_transform(self, formula):
	formula = o.transform(UnaryOperand("~",formula))
	return formula
	

if __name__ == '__main__':
    unittest.main()

