import fofTypes as f

def mrs_robinson(t1, t2):
	""" Tries to unifiy t1 to t2, which is t1 sigma = t2.
	    If the algorithm fails to find a unification, 
            an empty sigma is returned."""
	# FIXME: is breaking right?
	sigma = {}
	while substitute(t1,sigma) != substitute(t2,sigma):
		d1,d2 = get_disagreement_pair(substitute(t1,sigma),substitute(t2,sigma))
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
	for counter in range(len(terms)):
		if counter != (len(terms)-1):
		sigma = mrs_robinson(substitute(terms[counter],sigma),
				     substitute(terms[counter+1]),sigma) 	
	return sigma

def substitute(formula, sigma):
	""" sigma is a substition containing representations of 
	    a tree as the keys """
	if repr(formula) in sigma:
		formula = sigma[repr(formula)]
	else:
		for counter in range(len(formula.terms)):
			formula.terms[counter] = substitute(formula.terms[counter],sigma)
	return	formula
	
def get_disagreement_pair(t1, t2):
	""" gets the first unequal subterms of t1 and t2. 
	    Both must be terms in order for this algorithm to work."""
	if (t1 != t2): return t1,t2
	for counter in range(len(t1.terms)):
		return get_disagreement_pair(t1.terms[counter], t2.terms[counter])	

def occurs_in(t1, t2):
	""" returns true if t1 is a subtree of t2, otherwise false. """
	if t1 == t2:
		return True
	for x in t2.terms:
		if occurs_in(t1,x): return True
	return False			
