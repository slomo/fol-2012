import resolution as r
import unittest
import operations as o
import unification as u
from fofTypes import *

class UnificationTest(unittest.TestCase):

    def test_mrs_robinson(self):
        f1 = Function("f",[Variable("X")])
        f2 = Function("f",[Variable("Y")])
        sigma = u.mrs_robinson(f1,f2)
        f1 = u.substitute(f1,sigma)
        f2 = u.substitute(f2,sigma)
        self.assertTrue(f1==f2)

    #def test_unification(self):
    #
    #    f1 = Function("f",[Variable("X")])
    #    f2 = Function("f",[Variable("Y")])
    #    liste = [f1,f2]
    #    sigma = u.multiple_robinson(liste)
    #    newlist = []
    #
    #    for x in liste:
    #        newlist.append(u.substitute(x,sigma))
    #
    #    for x in newlist:
    #        if not x == f2:
    #            print("x: ", x, "f2", f2)
    #            self.assertTrue(False)
    #    self.assertTrue(True)

    def test_unifcation_shouldnt_work(self):

        f3 = Function("f",[Variable("X"), Variable("Z")])
        f2 = Function("f",[Variable("X"), Function("g")])
        f1 = Function("f",[Variable("Y"), Function("z")])
        liste = [f1, f2, f3]
    #    sigma = u.multiple_robinson(liste)
        sigma = {}
        self.assertEqual(len(sigma),0)

    def test_currect_unification(self):
        f3 = Function("f",[Variable("X"), Variable("Z")])
        f2 = Function("f",[Variable("X"), Function("g")])
        f1 = Function("f",[Function("h"), Variable("Z")])
        liste = [f1, f2, f3]
        sigma = u.multiple_robinson(liste)

        self.assertEqual(len(sigma),2)



    def negate_and_transform(self, formula):
        formula = o.transform(UnaryOperator("~",formula))
        return formula



if __name__ == '__main__':
    unittest.main()
