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
    if not isinstance(node.term, f.Identifier):
        pass
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
    print('Applying rule for ', transformations[node.op](node))
    if node.op in transformations:
        if isinstance(node, f.BinaryOperand):
            t = transformations[node.op](node)
            leftnode = transform(t.terms[0])
            rightnode = transform(t.terms[1])
            t.terms = leftnode, rightnode
        if isinstance(node, f.UnaryOperand):
            t = transformations[node.op](node)
            node = t
            transform(node)
        if isinstance(node, f.Identifier):
            return node
    else:
        node.terms = transform(node.terms[0]),transform(node.terms[1])
        return node
