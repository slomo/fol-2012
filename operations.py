import fofTypes as f
import unification as u
from copy import deepcopy

# helpers for unf transform
substitutions = {}

def gen_uniq_varname(variable):
    return variable.name  + "_" + str(id(variable))

def rewrite_binary(binary_formula, left, right, new_op):
    """ Reweriting a binary operand formula, from its current op to the new op,
        with negating the left and right formula, if requested"""

    [ left_formula, right_formula ] = binary_formula.terms

    if not left:
       left_formula = left_formula.negate()

    if not right:
       right_formula = right_formula.negate()

    return f.BinaryOperator(new_op, transform(left_formula), transform(right_formula))

def rewrite_quantor(quantor_formula, not_negated, new_quantor):

    global substitutions
    old = deepcopy(substitutions)

    for var in quantor_formula.variables:
        substitutions[var] = gen_uniq_varname(var)

    if not_negated:
        new_term = transform(quantor_formula.term)
    else:
        new_term = transform(quantor_formula.term.negate())

    new_vars = [ u.substitute(var,substitutions) for var in quantor_formula.variables ]

    substitutions = old

    return f.Quantor(new_quantor, new_vars, new_term)

# basic unf transforms

def alpha(left, right):
    return lambda formula: rewrite_binary(formula, left, right, "&")

def beta(left, right):
    return lambda formula: rewrite_binary(formula, left, right, "|")

def gamma(not_negated):
    return lambda formula: rewrite_quantor(formula, not_negated, '!')

def delta(not_negated):
    return lambda formula: rewrite_quantor(formula, not_negated, '?')

# non unf transforms

def double_negation(unary_formula):
    return transform(unary_formula.term.term)

def equivalance_rewrite(not_negated = True):

    def inner_function(eq_formula):
        [ left_formula, right_formula] = eq_formula.terms
        new_formula = f.BinaryOperator('|', left_formula.negate(), right_formula)
        if not_negated:
            return transform(new_formula)
        else:
            return transform(new_formula.negate())
    return inner_function


transformations = {

    '&'     : alpha(True, True),
    '~|'    : alpha(False, False),

    '|'     : beta(True, True),
    '~|'    : beta(False, False),
    '=>'    : beta(False, True),
    '<='    : beta(True, False),

    '!'     : gamma(True),
    '?'     : delta(True),

    '~'     : {
        '|'     : alpha(False, False),
        '=>'    : alpha(True, False),
        '<='    : alpha(False, True),
        '~&'    : alpha(True, True),

        '&'     : beta(False, False),
        '~|'    : beta(True, True),

        '?'     : gamma(False),
        '!'     : delta(False),

        '~'     : double_negation,

        '<=>'   : equivalance_rewrite(False),
        '<~>'   : equivalance_rewrite(),
    },

    '<=>'   : equivalance_rewrite(),
    '<~>'   : equivalance_rewrite(False),
}


def transform(formula):

    if type(formula) == f.Relation:
        return transform_relation(formula)

    if type(formula.negate()) == f.Relation:
        return (transform_relation(formula.negate())).negate()

    if type(formula) == f.UnaryOperator and formula.op == "~":
        return transformations['~'][formula.term.op](formula.term)

    else:
        return transformations[formula.op](formula)

# transformations on terms
def transform_relation(relation):

    global substitutions
    terms = [ u.substitute(term, substitutions) for term in relation ]
    return f.Relation(relation.name, terms)
