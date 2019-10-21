from algopy import bintree

def test_equal(B1, B2):
    if not(B1 or B2):
        return True
    return test_algo(B1, B2)

def test_algo(B1, B2):
    #TOBEFIXED
    pass



B_1 = bintree.BinTree(1, 
            bintree.BinTree(2, 
                bintree.BinTree(4, bintree.BinTree(8,None,None), None), 
                bintree.BinTree(5,None,bintree.BinTree(11,None,None))),
            bintree.BinTree(3, 
                bintree.BinTree(6,None,None), 
                bintree.BinTree(7, bintree.BinTree(14,None,bintree.BinTree(29,None,None)),None)))
            
B_2 = bintree.BinTree(1, 
            bintree.BinTree(2, 
                bintree.BinTree(4, bintree.BinTree(8,None,None), None), 
                bintree.BinTree(5,None,bintree.BinTree(11,None,None))),
            bintree.BinTree(3, 
                bintree.BinTree(6,None,None), 
                bintree.BinTree(7, bintree.BinTree(14,None,bintree.BinTree(29,None,None)),None)))

print(test_equal(B_1, B_2))