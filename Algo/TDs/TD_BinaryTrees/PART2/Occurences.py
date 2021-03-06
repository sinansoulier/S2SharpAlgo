from algopy import bintree
from importlib.machinery import SourceFileLoader
myfile = "/Users/francoissoulier/Desktop/AlgoTools/binary trees/bintrees_measures_2019-10.py"
measures = SourceFileLoader('measures', myfile).load_module()

#-------------------------------------------------------------------------------------------------

def __searchOcc(B, c, occ=""):
    if B.left == B.right:
        if B.key == c:
            return occ
        else:
            return ""
    else:
        res = __searchOcc(B.left, c, occ+'0')
        if res == "":
            res = __searchOcc(B.right, c, occ+'1')
        return res

#-------------------------------------------------------------------------------------------------

# T = [None]*(2**n), avec n la taille
# Creation of list using hierarchical representation

def __create_list(B, T, hier=1):
    
    l = len(T)                  # - Tests to build list
    if l-1 < hier:              #   over the different recursive
        L = [None]*(hier-l+1)   #   calls in the algorithm  
        T = T + L               # - Concatenation of lists to make it 
    T[hier] = B.key             #   bigger in case it is not big enough

    if not(B.left):
        if B.right:
            return __create_list(B.right, T, 2*hier+1)
        else:
            return T
    else:
        if B.right:
            return __create_list(B.left, T, 2*hier) + __create_list(B.right, T, 2*hier+1)
        else:
            return __create_list(B.left, T, 2*hier)

def object_to_list(B):
    if not(B):
        return None
    #T = [None]*(2**(measures.size(B)))
    
    return __create_list(B, [None])

    #return __create_list(B, T)


def __list_concat(L, l):
    for i in range(l):
        L.append(None)
    return L

def __create_list2(B, T, hier=1):
    if not(B):
        return T

    T = __list_concat(T, hier-len(T)+1)
    T[hier] = B.key

    return __create_list2(B.left, T, 2*hier) + __create_list2(B.right, T, 2*hier+1)


def object_to_list2(B):
    return __create_list2(B, [None])

#-------------------------------------------------------------------------------------------------

def list_to_object(T, i=1):
    if i >= len(T) or not(T[i]):
        return None
    else:
        B = bintree.BinTree(T[i], None, None)
        B.left = list_to_object(T, 2*i)
        B.right = list_to_object(T, 2*i+1)
        return B

#-------------------------------------------------------------------------------------------------

class BinTreeSize:
    def __init__(self, key, left, right, size):
        self.key = key
        self.left = left
        self.right = right
        self.size = size

def __sized_tree(B, B_sized):
    if not(B):
        return (None, 0)
    else:
        C = BinTreeSize(B.key, None, None, 1)
        (C.left, s_left) = __sized_tree(B.left)
        (C.right, s_right) = __sized_tree(B.right)
        C.size += s_left + s_right
        return (C, C.size)

def sized_tree(B):
    (C, _) = __sized_tree(B)
    return C

def load_tree(filename):
    f = open(filename)