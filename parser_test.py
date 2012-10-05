import unittest
import parser as p
from fofTypes import *

def _fofify(formula_str):
    return "fof(ax, axiom, " + formula_str + ")."

class PaserTest(unittest.TestCase):


    def test_quantor(self):
        string = _fofify(" ? [ X, Y, Z] : ( a | b ) ")

        result = p.parse_string(string)[0]
        quantor = result["formula"]
        self.assertEqual(type(quantor), Quantor)
        self.assertEqual(len(quantor.variables), 3)

if __name__ == '__main__':
    unittest.main()

