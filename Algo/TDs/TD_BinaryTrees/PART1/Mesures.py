from algopy import bintree

def size(B):
	if not(B):
		return 0
	else:
		return 1 + size(B.left) + size(B.right)

def height(B):
	if not(B):
		return -1
	else:
		return 1 + max(height(B.left), height(B.right))

def __lc(B, prof=0):
	if not(B):
		return (0, 0)
	else:
		if B.left == None and B.right == None:
			return (prof, 1)
		else:
			(lc_l, nl) = __lc(B.left, prof+1)
			(lc_r, nr) = __lc(B.right, prof+1)
			return (lc_l + lc_r, nl + nr)

def pm(B):
	if not(B):
		raise Exception("The binary tree B is emtpy")
	else:
		(lc, nb) = __lc(B)
		return lc/nb