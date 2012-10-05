import resolution as r
import unittest
from fofTypes import *

class ResolutionTest(unittest.TestCase):


    def test_a_or_not_a(self):

        formula = BinaryOperand("&",Identifier("a"),UnaryOperand("~",Identifier("a")))

        self.assertTrue(r.proof(formula))



if __name__ == '__main__':
    unittest.main()

