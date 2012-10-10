import fofTypes as f
from copy import deepcopy
import unification as u

boundvars = []

class Conjunction(set):

    def __repr__(self):
        return "<" +  set.__repr__(self)[13:-2] + ">"

class Disjunction(frozenset):

    free_vars = set()

    def __repr__(self):
       return "[" +  frozenset.__repr__(self)[13:-2] + "]"

    def replace(self, a, b):
        tmp = [ x for x in self if x != a ]
        tmp.append(b)
        return Disjunction(tmp)



def gen_free():
    i = 0
    while(True):
        i += 1
        var = "v"+str(i)
        if var not in boundvars:
            boundvars.append(var)
            yield var

def gen_free_func():
    i = 0
    while(True):
        i += 1
        var = "f"+str(i)
        if var not in boundvars:
            boundvars.append(var)
            yield var



def is_splittable(form):

    if type(form) == f.BinaryOperator:
        return True

    if type(form) == f.UnaryOperator  and type(form.term) != f.Relation:
        return True

    if type(form) == f.Quantor:
        return True
    return False


def proof(formula):

    unsplitted = Conjunction([Disjunction([formula])])
    splitted = Conjunction([])


    while len(unsplitted) > 0:

        disj = unsplitted.pop()
        splitted.add(disj)

        [  unsplitted.add(Disjunction(x)) for x in split_any(disj) ]

    return perform_resolution(splitted)

# returns: <[]>
def split_any(disjunction):

    result_set = []

    for formula in disjunction:
        if is_splittable(formula):
            print("formula: ", formula, " is splittable")
            #alpha
            if type(formula) == f.BinaryOperator and formula.op == "&":
                d = list(disjunction)
                d.remove(formula)
                d1 = deepcopy(d)
                d1.append(formula.terms[0])
                result_set.append(d1)

                d.append(formula.terms[1])
                result_set.append(d)
                break

            # is beta
            if type(formula) == f.BinaryOperator and formula.op == "|":
                d = list(disjunction)
                d.remove(formula)
                d.append(formula.terms[0])
                d.append(formula.terms[1])
                result_set.append(d)
                break
            
            # is gamma
            if type(formula) == f.Quantor and formula.op == '!':
                d = list(disjunction)
                d.remove(formula)
                rewrite = {}
                for var in formula.variables:
                    t = gen_free().__next__()
                    t = f.Variable(t)
                    rewrite[var] = t
                    disjunction.free_vars.add(t)
                d = u.substitute(formula.term, rewrite)
                d1 = deepcopy(d)
                result_set.append(d1)
                break

            # is delta
            if type(formula) == f.Quantor and formula.op == '?':
                d = list(disjunction)
                d.remove(formula)
                rewrite = {}
                for var in formula.variables:
                    t = gen_free_func().__next__()
                    t = f.Function(t,list(disjunction.free_vars))
                    rewrite[var] = t
                    disjunction.free_vars.add(t)
                d = u.substitute(formula.term, rewrite)
                d1 = deepcopy(d)
                result_set.append(d1)
                break

    return result_set

def is_tautology(d):

    for q in d:
        negate = f.UnaryOperator("~",q)
        if negate in d:
            return True
    return False


def negate(elem):
    # check weather i look for ~Z or Z
    if type(elem) is f.UnaryOperator:
        return elem.term
    else:
        return f.UnaryOperator("~",elem)


def resolute_any(disj, knf):

    results = set([])

    for other_disj in knf:

        results = results.union(resolute(disj, other_disj))

    return results

def resolute(disj_a, disj_b):

    result_set = set([])

    for formula in disj_a:
        negate_formula = formula.negate()

        if negate_formula in disj_b:
            d = list(disj_b)
            d.remove(negate_formula)
            d.extend(disj_a)
            d.remove(formula)

            if not is_tautology(d):
                print("Resoluting",disj_a,"with",disj_b,"to",d)
                result_set.add(Disjunction(d))

    return result_set


def perform_resolution(knf):
    knf = list(knf)
    for disj in knf:

        disjs = resolute_any(disj, deepcopy(knf))

        for resolutes in disjs:

            if len(resolutes) == 0:
                return True

            if not resolutes in knf:
                knf.append(resolutes)

    return False
