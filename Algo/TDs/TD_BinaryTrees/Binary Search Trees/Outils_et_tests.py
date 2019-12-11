from algopy import bintree

# 1.1 ---- Combien ?

def __nb_inter(B, a, b):
    if not(B):
        return 0

    else:
        if a < B.key:
            return __nb_inter(B.left, a, b)
            
        elif b >= B.key:
            return __nb_inter(B.right, a, b)

        else:
            return 1 + __nb_inter(B.left, a, b) + __nb_inter(B.right, a, b)
            

def nb_inter(B, a, b):
    return __nb_inter(B, a, b)

# 1.2 ---- Test

def __is_bst(B, inf, sup):
    if not(B):
        return True
    
    else:
        if B.key <= inf or B.key > sup:
            return False
        
        else:
            return __is_bst(B.left, inf, B.key) and __is_bst(B.right, B.key, sup)