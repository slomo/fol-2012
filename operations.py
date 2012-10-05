import parser
import fofTypes as f

def rewriteImplyR(node):
    leftnode = f.UnaryOperand('~', node.terms[0])
    node = f.BinaryOperand('|', leftnode, node.terms[1])
    return node

def rewriteImplyL(node):
    rightnode = f.UnaryOperand('~', node.terms[1])
    node = f.BinaryOperand('|', node.terms[0], rightnode)
    return node

def rewriteEquiv(node):
    leftnode = f.BinaryOperand('&',node.terms[0],node.terms[1])
    rightnode = f.BinaryOperand('&',f.UnaryOperand('~',node.terms[0]),f.UnaryOperand('~',node.terms[1]))
    node = f.BinaryOperand('|',leftnode,rightnode)
    return node

def rewriteNotEquiv(node):
    leftnode = f.BinaryOperand('&',node.terms[0],f.UnaryOperand('~',node.terms[1]))
    rightnode = f.BinaryOperand('&',f.UnaryOperand('~',node.terms[0]),node.terms[1])
    node = f.BinaryOperand('|',leftnode,rightnode)
    return node

def rewriteNotOr(node):
    leftnode = f.UnaryOperand('~',node.terms[0])
    rightnode = f.UnaryOperand('~',node.terms[1])
    node = f.BinaryOperand('&',leftnode,rightnode)
    return node

def rewriteNotAnd(node):
    leftnode = f.UnaryOperand('~',node.terms[0])
    rightnode = f.UnaryOperand('~',node.terms[1])
    node = f.BinaryOperand('|',leftnode,rightnode)
    return node

def rewriteNot(node):
    if isinstance(node.term, f.Identifier):
        return node
    if isinstance(node.term, f.UnaryOperand):
        node = node.term.term
    if isinstance(node.term, f.BinaryOperand):
        leftnode = f.UnaryOperand('~', node.term.terms[0])
        rightnode = f.UnaryOperand('~', node.term.terms[1])
        if node.term.op == '|':
            node = f.BinaryOperand('&', leftnode, rightnode)
        elif node.term.op == '&':
            node = f.BinaryOperand('|', leftnode, rightnode)
    return node




transformations = {
    '=>' : rewriteImplyR,
    '<=' : rewriteImplyL,
    '<=>' : rewriteEquiv,
    '<~>' : rewriteNotEquiv,
    '~&' : rewriteNotAnd,
    '~|' : rewriteNotOr,
    '~' : rewriteNot,

}

def transform(node):
    if isinstance(node, f.Identifier):
        return node
    if node.op in transformations:
        print('Applying rule for ', node.op,  ' leading to: \n'
              ,transformations[node.op](node))
        node = transformations[node.op](node)
        if node.op != '~':
            node.terms = transform(node.terms[0]),transform(node.terms[1])
        else:
            node.term = transform(node.term)
    else:
        node.terms = transform(node.terms[0]),transform(node.terms[1])
    return node
