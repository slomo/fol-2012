import parser
import fofTypes as f




def rewriteImplyR(node):
    node.op = '|'
    leftnode = f.UnaryOperand('~')
    leftnode.term = node.terms[0]
    node.terms = leftnode, node.terms[1]

def rewriteImplyL(node):
    node.op = '|'
    rightnode = f.UnaryOperand('~')
    rightnode.term = node.terms[1]
    node.terms = node.terms[0],rightnode

def rewriteEquiv(node):
    leftnode = f.BinaryOperand('&')
    leftnode.terms = node.terms[0],node.terms[1]
    rightnode = f.BinaryOperand('&')
    rightnode.terms = f.UnaryOperand('~'),f.UnaryOperand('~')
    rightnode.terms[0].term = node.terms[0]
    rightnode.terms[1].term = node.terms[1]
    node = f.BinaryOperand('|')
    node.terms = leftnode,rightnode

def rewriteNotEquiv(node):
    leftnode = f.BinaryOperand('&')
    rightnode = f.BinaryOperand('&')
    leftnode.terms = node.terms[0],f.UnaryOperand('~')
    leftnode.terms[1].term = node.terms[1]
    rightnode.terms = f.UnaryOperand('~'),node.terms[1]
    rightnode.terms[0].term = node.terms[0]
    node = f.BinaryOperand('|')
    node.terms = leftnode,rightnode

def rewriteNotOr(node):
    leftnode = f.UnaryOperand('~')
    leftnode.term = node.terms[0]
    rightnode = f.UnaryOperand('~')
    rightnode.term = node.terms[1]
    node = f.BinaryOperand('&')
    node.terms = leftnode,rightnode

def rewriteNotAnd(node):
    leftnode = f.UnaryOperand('~')
    leftnode.term = node.terms[0]
    rightnode = f.UnaryOperand('~')
    rightnode.term = node.terms[1]
    node = f.BinaryOperand('|')
    node.terms = leftnode,rightnode

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

