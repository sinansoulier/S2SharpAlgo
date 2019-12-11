from algopy import bintree

# 2.1 ---- Recherches
# 1°/ a) Min: Au bout du bord gauche de l'arbre
#        Max: Au bout du bord droit de l'arbre
#     b)

def minBST(B):
    while B.left:
        B = B.left
    return B.key()

def maxBST(B):
    if not(B.right):
        return B.key
    else:
        return maxBST(B.right)

    
# 2°/
# Récursif

def search_rec(B, x):
    if not(B):
        return None

    if x < B.key:
        return search_rec(B.left, x)
    elif x > B.key:
        return search_rec(B.right, x)
    else:
        return B


def search_iter(B, x):
    while B and B.key != x:
        if x > B.key:
            B = B.right
        else:
            B = B.left

    return B


# 2.2 ---- Insertion en feuille
# 1°/ 
# 2°/

def leaf_insert_rec(B, x):
    if not(B):
        return bintree.Bintree(x, None, None)
    
    else:
        if x > B.key:
            B.right = leaf_insert_rec(B.right, x)
        else:
            B.left = leaf_insert_rec(B.left, x)
        return B

def leaf_insert_iter(B, x):
    pass




# 2.3 ---- Suppression
def supp_max(B):
    if not(B.right):
        m = B.key
        B = B.left
        return m
    
    else:
        return supp_max(B.right)

def supp(B, x):
    if B:
        if x < B.key:
            supp(B.left, x)
        else:
            if x > B.key:
                supp(B.right, x)
            else:
                if not(B.left):
                    B = B.right
                else:
                    if not(B.right):
                        B = B.left
                    else:
                        B.key = supp_max(B.left)


# 2.4 ---- Insertion(root)
# 1°)
# 2°)

def cut(x, B, L, R):
    if not(B):
        L = None
        R = None
    else:
        if B.key <= x:
            L = B
            cut(x, B.right, B.right, R)
        else:
            D = B
            cut(x, B.left, L, B.left)

def root_insertion(x, B):
    B.key = x
    cut(x, B, B.left, B.right)
    return bintree.Bintree(B.key, B.left, B.right)