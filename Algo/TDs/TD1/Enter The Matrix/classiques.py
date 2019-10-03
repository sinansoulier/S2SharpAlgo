# Exercice 1.1 (Print)
# 1. Ecrire la fonction printmatrix(M) qui affiche la matrice M
# 2. Bonus : Ecrire la fonction prettyprintmatrix(M, d)

def printmatrix(M):
    for i in M:
        p_str = ""
        for j in M[i]:
            p_str += j + ' '
        print(p_str)

def initmatrix(l, c, val):
    M = []
    for i in range(c):
       arr = []
       for j in range(l):
           arr.append(val)
       M.append(arr)
    return M

import random
random.seed()
def buildmatrix(l, c, n):
    M = []
    for i in range(c):
       arr = []
       for j in range(l):
           arr.append(random.randint(0, n-1))
       M.append(arr)
    return M

Matr = buildmatrix(10, 10, 'V')
printmatrix(M)


def loadmatrix(filename):
    s = open(filename)
    L = s.readlines()
    M = []
    for i in L:
        M.append(splitL(i))
    return M

def splitL(S):
    L = []
    for i in S:
        if not (i == " " or i == "\\" or i == "n"):
            L.append(i)
    return L

# Exercice 1.3 (Addition de matrices)

def addmatrix(A, B):
    lenA, lenB, lenA0, lenB0 = len(A), len(B), len(A[0]), len(B[0])
    if not same_dim(A, B, lenA, lenB, lenA0, lenB0):
        raise Exception("The two matrices don't have the same dimension")

    M = []   
    for i in range(lenA):
        arr = []
        for j in range(lenA0):
            arr.append(A[i][j] + B[i][j])
        M.append(arr)
    return M

def same_dim(A, B, lenA, lenB, lenA0, lenB0):
    return lenA == lenB and lenA0 == lenB0

# Exercice 1.4 (Produit de matrices)

def mulmatrix(A, B):
    M = []
    lenA0 = len(A[0])
    lenB = len(B)
    if lenA0 != lenB:
        raise Exception("Error dimension")

    for i in range(len(A)):
        arr = []
        for j in range(len(B[0])):
            v = 0
            for k in range (lenA0):
                v += A[i][k]*B[k][j]
            arr.append(v)
        M.append(arr)
    return M
