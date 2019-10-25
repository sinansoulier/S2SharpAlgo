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
    
    #get smallest pair and store it in a variable
    small_pair = H[1]

    #swap this value with the last element of the Heap
    length_H = len(H)
    __swap(H, 1, length_H - 1)

    #pop the last value of the Heap, which is now the smallest value of the heap
    H.pop()
    
    #'Downheap' until the element that is in the first position finds its 'rightful' place
    if not(is_empty(H)):
        i = 1
        _2i = 2*i
        length_H -= 1

    __reorder(H, length_H)
    return small_pair

def __swap(H, i1, i2):
    """
    function that swaps two elements from a heap, given their indexes
    """
    swap = H[i1]
    H[i1] = H[i2]
    H[i2] = swap

"""def __reorder(H, length_H):
    
    #function that fixes the heap, in case its order relation is 'broken' 
    
    for i in range (1, length_H//2+1):
            _left_pos = 2*i
            _right_pos = _left_pos + 1

            if _left_pos < length_H:
                if _right_pos < length_H and H[_right_pos][0] < H[i][0] and H[_right_pos][0] < H[_left_pos][0]:
                    __swap(H, i, _right_pos)
                elif H[_left_pos][0] < H[i][0]:
                    __swap(H, i, _left_pos)"""
    
def __reorder(H, length_H):
    """
    function that fixes the heap, in case its order relation is 'broken' 
    """
    i = 1
    while i < length_H//2:
            _left_pos = 2*i
            _right_pos = _left_pos + 1

            if _left_pos < length_H:
                if _right_pos < length_H and H[_right_pos][0] < H[i][0] and H[_right_pos][0] < H[_left_pos][0]:
                    __swap(H, i, _right_pos)
                    i = _right_pos
                elif H[_left_pos][0] < H[i][0]:
                    __swap(H, i, _left_pos)
                    i = _left_pos
                else:
                    i = _left_pos

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
    while checker and i < length_T//2+1:
            _left_pos = 2*i
            _right_pos = _left_pos + 1

            if _left_pos < length_T:
                checker = _right_pos < length_T and T[_right_pos][1] > T[i][1] or T[_left_pos][1] > T[i][1]
            i += 1
    return checker
    
def heap_sort(L):
    """ sorts the associative list L in increasing order according to values 
    
        :param L: a list containing pairs (element, value)
        :rtype: (any, num) list (the new list sorted)
    """
    return __sort_heap(L)

def __sort_heap(L):
    H = Heap()
    for i in L:
        push(H, i[0], i[1])
    L_r = []
    for i in range(1, len(H)):
        tup = pop(H)
        L_r.append((tup[1], tup[0]))
    return L_r 
