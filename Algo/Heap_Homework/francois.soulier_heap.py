__license__ = 'Nathalie (c) EPITA'
__docformat__ = 'reStructuredText'
__revision__ = '$Id: heap.py 2019-10-14'

"""
Heap homework
2019 - S2#
@author: francois.soulier
"""

#given function

def Heap():
    """ returns a fresh new empty heap
    
       :rtype: list (heap)
    """
    return [None]
    
###############################################################################
# Do not change anything above this line, except your login!
# Do not add any import


    
def is_empty(H):
    """ tests if the heap H is empty
    
       :param H: the heap
       :type H: list (hierachical rep. of bintree)
       :rtype: bool
    """
    return H == [None]

def push(H, elt, val):
    """ adds the pair (val, elt) to heap H (in place: no need to return H)
    
       :param H: The heap
       :type H: list (hierachical rep. of bintree)
       :param elt: The element to add
       :type elt: any
       :param val: The value associated to elt
       :type val: int or float
    """
    _tuple = (val, elt)
    H.append(_tuple)
    lengthH = len(H)
    i = lengthH - 1
    i_div2 = i//2

    while H[i_div2] != None and i > 0 and H[i][0] < H[i_div2][0]:
            __swap(H, i, i_div2)
            i = i//2
            i_div2 = i//2
    

def pop(H):
    """ removes and returns the pair of smallest value in the heap H
    
       :param H: The heap
       :type H: list (hierachical rep. of bintree)
       :rtype: (num, any) (the removed pair)
    """
    if is_empty(H):
        raise Exception("The heap is empty")
    
    
    small_pair = H[1]
    length_H = len(H)-1
    __swap(H, 1, length_H)
    H.pop()

    if not(is_empty(H)):
        i = 1
        while i <= length_H//2:
            _left_pos = 2*i
            _right_pos = _left_pos + 1
            
            if _right_pos < length_H and H[_right_pos][0] < H[i][0] and H[_right_pos][0] < H[_left_pos][0]:
                __swap(H, i, _right_pos)
                i = _right_pos
            elif _left_pos < length_H and H[_left_pos][0] < H[i][0]:
                __swap(H, i, _left_pos)
                i = _left_pos
            else:
                i = _left_pos

    return small_pair

def __swap(H, i1, i2):
    """
    function that swaps two elements from a heap (or a list), given their indexes
    """
    swap = H[i1]
    H[i1] = H[i2]
    H[i2] = swap


#---------------------------------------------------------------
def is_heap(T):
    """ tests whether the complete tree T is a heap
    
       :param T: a complete tree in hierarchical representation
       :type T: list (hierachical rep. of bintree)
       :rtype: bool
    """
    if not(T):
        return False
    checker = T[0] == None
    if is_empty(T):
        return True

    i = 1
    length_T = len(T)
    while checker and i <= length_T//2:
            _left_pos = 2*i
            _right_pos = _left_pos + 1

            if _right_pos < length_T:
                checker = T[_right_pos][0] > T[i][0] and T[_left_pos][0] > T[i][0]
                
            elif _left_pos < length_T:
                checker = T[_left_pos][0] > T[i][0]
            i += 1
    return checker
    
def heap_sort(L):
    """ sorts the associative list L in increasing order according to values 
    
        :param L: a list containing pairs (element, value)
        :rtype: (any, num) list (the new list sorted)
    """
    H = Heap()
    for i in L:
        push(H, i[0], i[1])
    L_r = []
    for i in range(1, len(H)):
        tup = pop(H)
        L_r.append((tup[1], tup[0]))
    return L_r 
