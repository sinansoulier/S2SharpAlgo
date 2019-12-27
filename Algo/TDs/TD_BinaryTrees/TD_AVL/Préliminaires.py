from algopy import bintree
from algopy import avl

def __toAVL(B):
    if not(B):
        return (None, -1)
    else:
        (left, hl) = __toAVL(B.left)
        (right, hr) = __toAVL(B.right)
        return (avl.AVL(B.key, B.left, B.right, hl-hr), 1 + max(hl, hr))

def toAVL(B):
    (_AVL,_) = __toAVL(B)
    return _AVL