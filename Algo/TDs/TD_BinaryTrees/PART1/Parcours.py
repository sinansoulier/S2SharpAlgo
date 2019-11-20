from algopy import bintree

def dft(B):
    if not(B):
        print('_')
    else:
        print('<',B.key,',')
        dft(B.left)
        print(',')
        dft(B.right)
        print('>')

def bfs(B):
    pass