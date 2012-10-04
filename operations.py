import parser
import fofTypes as f




def rewriteImplyR(node):
    node.op = '|'
    node.terms[0] = f.UnaryOperand('~', node.terms[0])

def rewriteImplyL(node):
    node.op = '|'
    temp_terms = node.terms[1]
    node.terms[1] = f.UnaryOperand('~')
    node.terms[1].term = temp_terms

def rewriteEquiv(node):
    leftnode = f.BinaryOperand('&')
    leftnode.terms[0] = node.terms[0]
    leftnode.terms[1] = node.terms[1]
    rightnode = f.BinaryOperand('&')
    rightnode.terms[0] = f.UnaryOperand('~')
    rightnode.terms[0].term = node.terms[0]
    rightnode.terms[1] = f.UnaryOperand('~')
    rightnode.terms[1].term = node.terms[1]
    node = f.BinaryOperand('|')
    node.terms[0] = leftnode
    node.terms[1] = rightnode

def rewriteNotEquiv(node):
    leftnode = f.BinaryOperand('&')
    rightnode = f.BinaryOperand('&')
    leftnode.terms[0] = node.terms[0]
    leftnode.terms[1] = f.UnaryOperand('~')
    leftnode.terms[1].term = node.terms[1]
    rightnode.terms[0] = f.UnaryOperand('~')
    rightnode.terms[0].term = node.terms[0]
    rightnode.terms[1] = node.terms[1]
    node = f.BinaryOperand('|')
    node.terms[0] = leftnode
    node.terms[1] = rightnode

def rewriteNotOr(node):
    leftnode = f.UnaryOperand('~')
    leftnode = node.term[0]
    rightnode = f.UnaryOperad('~')
    rightnode = node.term[1]
    node = f.BinaryOperand('&')
    node.terms[0] = leftnode
    node.terms[1] = rightnode

def rewriteNotAnd(node):
    leftnode = f.UnaryOperand('~')
    leftnode = node.term[0]
    rightnode = f.UnaryOperand('~')
    rightnode = node.term[1]
    node = f.BinaryOperand('|')
    node.terms[0] = leftnode
    node.terms[1] = rightnode

transformations = {
    '=>' : rewriteImplyR,
    '<=' : rewriteImplyL,
    '<=>' : rewriteEquiv,
    '<~>' : rewriteNotEquiv,
    '~&' : rewriteNotAnd,
    '~|' : rewriteNotOr,

}
