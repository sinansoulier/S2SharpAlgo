from algopy import bintree

#Arbre complet (perfect tree)
#noeuds internes = points doubles ET feuilles au même niveau
#Tous les niveaux sont remplis

def __perfect_test1(B, height):
    if not(B.left):
        if not(B.right):
            return height == 0
        else:
            return False
    else:
        if not(B.right):
            return False
        else:
            return __perfect_test1(B.left, height-1) and __perfect_test1(B.right, height-1)

def perfect_test1(B):
    if not(B):
        return True
    T = B
    height = 0
    while T.left:
        height += 1
        T = T.left    

    return __perfect_test1(B, height)
    
        
        
    
     
