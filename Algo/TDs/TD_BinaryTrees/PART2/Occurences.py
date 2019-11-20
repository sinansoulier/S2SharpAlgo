from algopy import algopy

def __searchOcc(B, c, occ=""):
    if B.left == B.right:
        if B.key == c:
            return occ
        else:
            return ""
    else:
        res = __searchOcc(B.left, c, occ+'0')
        if res == "":
            res = __searchOcc(B.right, c, occ+'1')
        return res


# T = [None]*(2**n), avec n la taille