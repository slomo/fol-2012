import fofTypes as f
from copy import deepcopy

def is_splittable(form):

    if type(form) == f.BinaryOperand:
        return True

    if type(form) == f.UnaryOperand  and type(form.term) != f.Identifier:
        return True

    return False


def proof(formula):

    splittables = set([frozenset([formula])])
    result = []

    while len(splittables) > 0:

        disj = splittables.pop()

        [ splittables.add(frozenset(x)) for x in split_any(disj) ]

        result.append(disj)

    print("splitted formulas", result)

    return resolute(result)

# returns: <[]>
def split_any(disjunction):

    result_set = []

    for formula in disjunction:
        if is_splittable(formula):

            if type(formula) == f.UnaryOperand:
                if type(formula.term) == f.UnaryOperand:
                    d = list(disjunction)
                    d.remove(formula)
                    d.append(formula.term.term)
                    break

            #alpha
            if type(formula) == f.BinaryOperand and formula.op == "&":
                d = list(disjunction)
                d.remove(formula)
                d1 = deepcopy(d)
                d1.append(formula.terms[0])
                result_set.append(d1)

                d.append(formula.terms[1])
                result_set.append(d)
                break

            # is beta
            if type(formula) == f.BinaryOperand and formula.op == "|":
                d = list(disjunction)
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

                    d = list(other_disj)
                    d.remove(target)
                    d.extend(disj)
                    d.remove(elem)

                    d = frozenset(d)

                    if len(d) == 0:
                        return True
                    if not (d in knf) and not is_tautology(d):
                        print("Resoluting",disj,"with",other_disj,"to",d)
                        knf.append(d)

    return False
