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

        if all([ type(x) == f.Relation or type(x.negate()) == f.Relation for x in disj]):
            splitted.add(disj)

        print("split",split_any(disj))
        [ unsplitted.add(Disjunction(x)) for x in split_any(disj) ]

        print("unsplitted", disj)

    # Phase 2
    knf = splitted

    iterations = 300

    print("atomics",knf)

    for i in range(iterations):

        resolvents = resolute_all(deepcopy(knf))

        for disj in resolvents:

            if len(disj) == 0:
                return True

            knf.add(disj)

    return None

# returns: <[]>
def split_any(disjunction):

    result_set = []

    for formula in disjunction:
        if is_splittable(formula):
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
                d.append(s_wrapper(formula.term, rewrite))
                result_set.append(d)
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
                d.append(s_wrapper(formula.term, rewrite))
                result_set.append(d)
                break

    return result_set

def is_tautology(d):

    for q in d:
        negate = f.UnaryOperator("~",q)
        if negate in d:
            return True
    return False


def resolute_all(knf):

    results = set([])

    for disj in knf:
        for other_disj in knf:
            results.update(resolute(disj, other_disj))

    return results

def resolute(disj_a, disj_b):

    result_set = set([])

    for formula in disj_a:
        for other_formula in disj_b:

            if type(other_formula) == f.UnaryOperator and type(formula) == f.Relation:
                sigma = u.mrs_robinson(other_formula.term, formula)

                list_disj_a = []
                list_disj_b = []

                # simple case resolution possible
                if other_formula.term == formula:

                    list_disj_a = list(disj_a)
                    list_disj_b = list(disj_b)

                    list_disj_a.remove(formula)
                    list_disj_b.remove(other_formula)


                # difficult case resolution with unification  possible
                elif sigma:

                    list_disj_a = [ s_wrapper(x, sigma) for x in disj_a if not x is formula ]
                    list_disj_b = [ s_wrapper(x, sigma) for x in disj_b if not x is other_formula ]

                resolvente = Disjunction(list_disj_a + list_disj_b)

                if not is_tautology(resolvente):
                    print("Resoluting",disj_a,"with",disj_b,"to",resolvente)
                    result_set.add(resolvente)

            else:
                continue

    return result_set


def s_wrapper(formula, sups):

    if type(formula) == f.Relation:
        return u.substitute(formula, sups)
    elif type(formula) == f.UnaryOperator and type(formula.term) == f.Relation:
        return f.UnaryOperator("~", u.substitute(formula.term, sups))
    else:
        assert(False)


