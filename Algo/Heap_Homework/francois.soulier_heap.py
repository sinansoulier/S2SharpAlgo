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
    if not(is_empty(H)):
        _tuple = (val, elt)
        H.append(_tuple)
        lengthH = len(H)
        i = lengthH - 1
        i_div2 = int(i/2)

        while H[i_div2] and H[i][0] < H[i_div2][0]:
            __swap(H, i, i_div2)
            i = int(i/2)
            i_div2 = int(i/2)
    
def __swap(H, i1, i2):
    """
    function that swaps two elements from a heap, given their indexes
    """
    swap = H[i1]
    H[i1] = H[i2]
    H[i2] = swap
    
def pop(H):
    """ removes and returns the pair of smallest value in the heap H
    
       :param H: The heap
       :type H: list (hierachical rep. of bintree)
       :rtype: (num, any) (the removed pair)
    """
    if is_empty(H):
        return None
    
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

    while _2i < length_H and H[i][0] > H[_2i][0]:
        if _2i + 1 < length_H and H[i][0] > H[_2i][0]:
            __swap(H, i, _2i+1)
            i = 2*i + 1
            _2i = 2*i
        else:
            __swap(H, i, _2i+1)
            i *= 2
            _2i = 2*i

    return small_pair


#---------------------------------------------------------------
def is_heap(T):
    """ tests whether the complete tree T is a heap
    
       :param T: a complete tree in hierarchical representation
       :type T: list (hierachical rep. of bintree)
       :rtype: bool
    """
    #FIXME
    pass
    
def heap_sort(L):
    """ sorts the associative list L in increasing order according to values 
    
        :param L: a list containing pairs (element, value)
        :rtype: (any, num) list (the new list sorted)
    """
    #FIXME
    pass
