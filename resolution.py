import fofTypes as f
from copy import deepcopy

def is_splittable(form):

    if type(form) == f.BinaryOperand:
        return True

    if type(form) == f.UnaryOperand  and type(form.term) != f.Identifier:
        return True

    return False


def proof(formula):

    clauses = [[formula]]

    # FIXME: i am so dumb
    for i in range(20):

        new_clauses = []
        [ new_clauses.extend(split_any(x)) for x in clauses ]

        #import pdb; pdb.set_trace()
        clauses = new_clauses

    noDupes = []
    [noDupes.append(i) for i in clauses if not noDupes.count(i)]

    print("splitted formulas", noDupes)

    return resolute(noDupes)

# returns: <[]>
def split_any(disjunction):

    result_set = [ disjunction ]

    for formula in disjunction:
        if is_splittable(formula):

            if type(formula) == f.UnaryOperand:
                if type(formula.term) == f.UnaryOperand:
                    d = deepcopy(disjunction).remove(formula)
                    d.append(formula.term.term)
                    break

            #alpha
            if type(formula) == f.BinaryOperand and formula.op == "&":
                d = deepcopy(disjunction)
                d.remove(formula)
                d1 = deepcopy(d)
                d1.append(formula.terms[0])
                result_set.append(d1)

                d.append(formula.terms[1])
                result_set.append(d)
                break

            # is beta
            if type(formula) == f.BinaryOperand and formula.op == "|":
                d = deepcopy(disjunction)
                d.remove(formula)
                d.append(formula.terms[0])
                d.append(formula.terms[1])
                result_set.append(d)
                break

    return result_set


def is_tautology(d):

    for q in d:
        negate = f.UnaryOperand("~",q)
        if negate in d:
            return True
    return False



def resolute(knf):

    for disj in knf:

        for elem in disj:

            # check weather i look for ~Z or Z
            if type(elem) is f.UnaryOperand:
                target = elem.term
            else:
                target = f.UnaryOperand("~",elem)

            for other_disj in deepcopy(knf):
                if target in other_disj:

                    d = deepcopy(other_disj)
                    d.remove(target)
                    d.extend(disj)
                    d.remove(elem)
                    noDupes = []
                    [noDupes.append(i) for i in d if not noDupes.count(i)]
                    d = noDupes

                    if len(d) == 0:
                        return True
                    if not (d in knf) and not is_tautology(d):
                        print("Resoluting",disj,"with",other_disj,"to",d)
                        knf.append(d)

    return False
