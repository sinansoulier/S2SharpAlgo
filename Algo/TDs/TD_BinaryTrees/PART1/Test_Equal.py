from algopy import bintree

def test_equal(B1, B2):
    if B1 and B2:
        if B1.key == B2.key:
            return test_equal(B1.left, B2.left) and test_equal(B1.right, B2.right)
        return False
    return not(B1 or B2)


