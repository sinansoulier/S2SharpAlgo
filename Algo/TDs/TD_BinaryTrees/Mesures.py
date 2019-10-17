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