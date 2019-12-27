from algopy import avl

def lr(A):   #left rotation = rg
    aux = A.right
    A.right = aux.left
    aux.left = A
    desq = aux.bal
    
    #if desq == 0:
    #    aux.bal = 1
    #    A.bal = -1
    #else:
    #    aux.bal = 0
    #    A.bal = 0
    
    A.bal = -1 -aux.bal
    aux.bal = 1+ aux.bal

    return aux

def rr(A):
    pass

def lrr(A):
    pass

def rlr(A):
    pass

def insert1(x, A):
    if not(A):
        return (avl.AVL(x, None, None, 0), True)
    
    else:
        if x == A.key:
            return (A, False)
        elif x < A.key:
            (A.left, dh) = insert(x, A.left)
            if not(dh):
                return (A, False)
            else:
                A.bal += 1
                if A.bal == 0:
                    return (A, False)
                elif A.bal == 1:
                    return (A, True)
                elif A.bal == 2:
                    if A.left.bal == 1:
                        rr(A)
                    elif A.left.bal == -1:
                        lrr(A)
                    return (A, False)


#correction

def insert(A,x):
    if not(A):
        return (avl.AVL(x, None, None, 0), True)
    
    elif x == A.key:
        return (A, False)
    
    elif x < A.key:
        (A.left, dh) = insert(A.left, x)
        
        if not(dh):
            return (A, False)
        
        else:
            A.bal += 1
            
            if A.bal == 0:
                return(A, False)
            
            elif A.bal == 1:
                return (A, True)
            
            else:
                if A.left.bal == 1:
                    A = rr(A)
                else:
                    A = lrr(A)
                return (A, False)
    else:
        pass
        #Same structure
        #...


def delete(A, x):
    if not(A):
        return None
    else:
        if x == A.key:
            if not(A.left or A.right) or A.left and not(A.right):
                return A.left
            elif A.right and not(A.left):
                return A.right
            else:
                A.key = max(A.left)
                x = A.key
        
        elif x <= A.key:
            (A.left, dh) = delete(A.left)
            if not(dh):
                return (A, False)
            else:
                A.bal -= 1
                if A.bal == 0:
                    return (A, True)
                elif A.bal == -1:
                    return (A, False)
                else:
                    if A.right.bal == -1:
                        A = lr(A)
                        return (A, True)
                    elif A.right.bal == 0:
                        A = lr(A)
                        return (A, False)
                    else:
                        A = rlr(A)
                        return (A, True)
        
        else:
            pass