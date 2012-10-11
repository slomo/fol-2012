import fofTypes as f
from copy import deepcopy


def mrs_robinson(t1, t2):
    """ Tries to unifiy t1 to t2, which is t1 sigma = t2.
        If the algorithm fails to find a unification,
            an empty sigma is returned."""
    sigma = {}

    while not substitute(t1,sigma) == substitute(t2,sigma):
        d1,d2 = get_disagreement_pair(substitute(t1,sigma),substitute(t2,sigma))
        if not d1 and not d2:
            return {}
        if isinstance(d1,f.Variable):
            if occurs_in(d1,d2):
                return {}
            sigma.update({d1:d2})
        elif isinstance(d2,f.Variable):
            if occurs_in(d2,d1):
                return {}

            sigma.update({d2:d1})
        else:   return {}
    return sigma

def multiple_robinson(terms):
    """ Returns the most general unifier for this list of terms. """
    sigma = {}
    for x in terms:
        if type(x) != f.Function:
            return sigma
    for counter in range(len(terms)):
        if counter != (len(terms)-1):
            sigma = mrs_robinson(substitute(terms[counter],sigma),
                             substitute(terms[counter+1],sigma))
    return sigma

def substitute(term, sigma):
    """ sigma is a substition containing representations of
        a tree as the keys """

    #import pdb
    #pdb.set_trace()
    if term in sigma:
        return sigma[term]

    else:
        if type(term) == f.Variable:
            return term
        else:
            new_terms = [ substitute(child, sigma) for child in term ]
            if type(term) == f.Function:
                return f.Function(term.name, new_terms)

            elif type(term) == f.Relation:
                return f.Relation(term.name, new_terms)

            elif type(term) == f.BinaryOperator:
                [t1, t2] = new_terms
                return f.BinaryOperator(term.op, t1, t2)

            elif type(term) == f.UnaryOperator:
                [ t1 ] = new_terms
                return f.UnaryOperator("~", t1)

            elif type(term) == f.Quantor:
                [ t1 ] = new_terms
                return f.Quantor(term.op, term.variables, t1)

def get_disagreement_pair(t1, t2):
    """ gets the first unequal subterms of t1 and t2.
        Both must be terms in order for this algorithm to work."""
    # FIXME: Doesn't check on free variable occurences
    if (t1.name != t2.name):
        return t1,t2
    elif type(t1) != f.Variable and type(t2) != f.Variable:

        if len(t1.terms) != len(t2.terms):
            return t1, t2

        for counter in range(len(t1.terms)):
            dis_pair = get_disagreement_pair(t1.terms[counter], t2.terms[counter])

            if dis_pair != (None, None):
                return dis_pair
    return  None,None

def occurs_in(t1, t2):
    """ returns true if t1 is a subtree of t2, otherwise false. """
    if repr(t1) in repr(t2): return True
    return False
