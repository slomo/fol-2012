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
    return noDupes


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
                d1 = deepcopy(d).append(formula.terms[0])
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


def resolute(knf):

    for disj in knf:

        for elem in disj:

            if type(elem) is UnaryOperand:
                target = elem.term
            else:
                target = UnaryOperand("~",elem)

            for other in deepcopy(knf):

                if target in other:
                    d = deepcopy(other)
                    d.remove(target)
                    d.extend(disj)
                    d.remove(elem)
                    knf.append(d)

