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

    def test_unification(self):

        f1 = Function("f",[Variable("X")])
        f2 = Function("f",[Variable("Y")])
        liste = [f1,f2]
        sigma = u.multiple_robinson(liste)
        newlist = []
        for x in liste:
            newlist.append(u.substitute(x,sigma))
        print("newlist", newlist)
        for x in newlist:
            if x != f2:
                print("x: ", x, "f2", f2)
                self.assertTrue(False)
        self.assertTrue(True)

    def negate_and_transform(self, formula):
        formula = o.transform(UnaryOperator("~",formula))
        return formula



if __name__ == '__main__':
    unittest.main()
