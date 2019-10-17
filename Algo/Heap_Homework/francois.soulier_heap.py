__license__ = 'Nathalie (c) EPITA'
__docformat__ = 'reStructuredText'
__revision__ = '$Id: heap.py 2019-10-14'

"""
Heap homework
2019 - S2#
@author: login
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
    #FIXME
    pass

def push(H, elt, val):
    """ adds the pair (val, elt) to heap H (in place: no need to return H)
    
       :param H: The heap
       :type H: list (hierachical rep. of bintree)
       :param elt: The element to add
       :type elt: any
       :param val: The value associated to elt
       :type val: int or float
    """
    #FIXME
    pass
    
def pop(H):
    """ removes and returns the pair of smallest value in the heap H
    
       :param H: The heap
       :type H: list (hierachical rep. of bintree)
       :rtype: (num, any) (the removed pair)
    """
    #FIXME
    pass

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
