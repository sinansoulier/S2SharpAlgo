from algopy import bintree
import Occurences

B_1 = bintree.BinTree(1,
                bintree.BinTree(2,
                    bintree.BinTree(4, bintree.BinTree(8,None,None), None),
                    bintree.BinTree(5,None,bintree.BinTree(11,None,None))),
                bintree.BinTree(3,
                    bintree.BinTree(6,None,None),
                    bintree.BinTree(7, bintree.BinTree(14,None,None),None)))

B_2 = bintree.BinTree(1,
            bintree.BinTree(2,
                bintree.BinTree(4, bintree.BinTree(8,None,None), None),
                bintree.BinTree(5,None,bintree.BinTree(11,None,None))),
            bintree.BinTree(3,
                bintree.BinTree(6,None,None),
                bintree.BinTree(7, bintree.BinTree(14,None,bintree.BinTree(29,None,None)),None)))

print(Occurences.object_to_list2(B_1),"\n\n")
print(Occurences.object_to_list2(B_2))