import parser
import fofTypes as f

def rewriteImplyR(node):
    leftnode = f.UnaryOperand('~', node.terms[0])
    node = f.BinaryOperand('|', leftnode, node.terms[1])

def rewriteImplyL(node):
    rightnode = f.UnaryOperand('~', node.terms[1])
    node = f.BinaryOperand('|', node.terms[0], rightnode)

def rewriteEquiv(node):
    leftnode = f.BinaryOperand('&',node.terms[0],node.terms[1])
    rightnode = f.BinaryOperand('&',f.UnaryOperand('~',node.terms[0]),f.UnaryOperand('~',node.terms[1]))
    node = f.BinaryOperand('|',leftnode,rightnode)

def rewriteNotEquiv(node):
    leftnode = f.BinaryOperand('&',node.terms[0],f.UnaryOperand('~',node.terms[1]))
    rightnode = f.BinaryOperand('&',f.UnaryOperand('~',node.terms[0]),node.terms[1])
    node = f.BinaryOperand('|',leftnode,rightnode)

def rewriteNotOr(node):
    leftnode = f.UnaryOperand('~',node.terms[0])
    rightnode = f.UnaryOperand('~',node.terms[1])
    node = f.BinaryOperand('&',leftnode,rightnode)

def rewriteNotAnd(node):
    leftnode = f.UnaryOperand('~',node.terms[0])
    rightnode = f.UnaryOperand('~',node.terms[1])
    node = f.BinaryOperand('|',leftnode,rightnode)

transformations = {
    '=>' : rewriteImplyR,
    '<=' : rewriteImplyL,
    '<=>' : rewriteEquiv,
    '<~>' : rewriteNotEquiv,
    '~&' : rewriteNotAnd,
    '~|' : rewriteNotOr,

}

def transform(node):
    if hasattr(node, 'terms'):
        if node.terms[0]:
                transform(node.terms[0])
        if node.terms[1]:
                transform(node.terms[1])
    if hasattr(node, 'term'):
            transform(node.term)
    if hasattr(node, 'op'):
        if node.op in transformations:
            transformations[node.op](node)

