import fofTypes as f
from copy import deepcopy

def mrs_robinson(t1, t2):
	""" Tries to unifiy t1 to t2, which is t1 sigma = t2.
	    If the algorithm fails to find a unification, 
            an empty sigma is returned."""
	sigma = {}
        if type(t1) != f.Function or type(t2) != f.Function: return sigma
	while repr(substitute(t1,sigma)) != repr(substitute(t2,sigma)):
 		d1,d2 = get_disagreement_pair(substitute(t1,sigma),substitute(t2,sigma))
		if not d1 and not d2: return {}
		if isinstance(d1,f.Variable):
			if occurs_in(d1,d2):
				return {}
			sigma.update({repr(d1):d2})
		elif isinstance(d2,f.Variable):
			if occurs_in(d2,d1):
				return {}
			
			sigma.update({repr(d2):d1})
		else:	return {}
	return sigma 

def multiple_robinson(terms):
	""" Returns the most general unifier for this list of terms. """
	sigma = {}
	for x in terms:
		if type(x) != f.Function: return sigma
	for counter in range(len(terms)):
		if counter != (len(terms)-1):
			sigma = mrs_robinson(substitute(terms[counter],sigma),
				     	     substitute(terms[counter+1],sigma)) 	
	return sigma

def substitute(formula, sigma):
	""" sigma is a substition containing representations of 
	    a tree as the keys """
	term = deepcopy(formula)
	if repr(term) in sigma:
		term = sigma[repr(formula)]
	else:
		if type(term) == f.Function:
			for counter in range(len(term.terms)):
				if repr(term.terms[counter]) in sigma:
					term.terms[counter] = substitute(term.terms[counter],sigma)
		else:
			if repr(term) in sigma:
				term = sigma[repr(term)]
	return	term
	
def get_disagreement_pair(t1, t2):
	""" gets the first unequal subterms of t1 and t2. 
	    Both must be terms in order for this algorithm to work."""
	# FIXME: Doesn't check on free variable occurences
	if (t1.name != t2.name): return t1,t2
	elif type(t1) == f.Function and type(t2) == f.Function:
		for counter in range(len(t1.terms)):
			return get_disagreement_pair(t1.terms[counter], t2.terms[counter])
	return	None,None 

def occurs_in(t1, t2):
	""" returns true if t1 is a subtree of t2, otherwise false. """
	if repr(t1) in repr(t2): return True
	return False
