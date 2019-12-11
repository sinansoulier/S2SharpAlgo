from algopy import bintree

class BinTreeSize:
    def __init__(self, key, left, right, size):
        self.key = key
        self.left = left
        self.right = right
        self.size = size

def __addBSTSize(x, B):
    if not(B):
        return (BinTreeSize(x, None, None, 1), True)
    else:
        if B.key == x:
            return (B, False)
        else:
            if B.key < x:
                (B.left, inserted) = __addBSTSize(x, B.left)
            else:
                (B.right, inserted) = __addBSTSize(x, B.right)
            if inserted:
                B.size += 1
            return (B, inserted)

#------------------------------------------------------------------------

#   Abtsract study:
#   nth: BST x Integer -> Element
#   nth(B, n) is-defined-iff    1 <= n <= size(B)
#
#   n = size(L) + 1 => nth(<r, L, R>, k) = r
#   n < size(L) + 1 => nth(<r, L, R>, k) = nth(L, n)
#   n > size(L) + 1 => nth(<r, L, R>, k) = nth(R, k-size(G)-1)

def nthBST(B, k):
    if B.left:
        _size_left = B.left.size
        if k == _size_left:
            return B
        else:
            if k < _size_left:
                return nthBST(B.left, k)
            else:
                return nthBST(B.right, k-_size_left-1)
    else:
        if k == 1:
            return B
        else:
            return nthBST(B.right, k-1)


def median(B):
    if B:
        return nthBST(B, (B.size+1)//2).key
    else:
        return None