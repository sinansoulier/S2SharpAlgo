import classiques
def getMax(L):
    if L:
        max = L[0]
        for i in L:
            if i > max:
                max = i
        return max
    return None

def getMin(L):
    if L:
        min = L[0]
        for i in L:
            if i < min:
                min = i
        return min
    return None

def getMinPos(L):
    minPos = 0
    for i in range(len(L)):
        if L[i] < L[minPos]:
            minPos = i
    return minPos

def getMaxPos(L):
    maxPos = 0
    for i in range(len(L)):
        if L[i] > L[maxPos]:
            maxPos = i
    return maxPos

# Exercice 2.1 (Minimax)
# Consigne : Ecrire une fonction qui retourne la position de la valeur minimale parmi les maximums de chaque ligne d'une matrice d'entiers non vide
# Forme : (x(colonne), y(ligne))

def posMinimax(M):
    if M:
        x, y = 0, getMaxPos(M[0])
        for i in range(len(M)):
            j = getMaxPos(M[i])
            if M[i][j] < M[x][y]:
                x, y = i, j
        return (x, y)
    return (-1, -1)

M_minimax1 = [[1, 24, 12, 18, 4],
 [10, 15, 15, 0, 18],
 [8, 14, 0, 16, 2],
 [22, 4, 8, 14, 22],
 [19, 7, 23, 5, 5]]

M_minimax2 = [[1, 24, 12, 18, 4],
 [10, 15, -15, 0, 18],
 [-8, 14, 0, 16, 2],
 [22, 16, 8, 14, 22],
 [19, -7, 23, 5, -5]]

a, b = posMinimax(M_minimax1)
c, d = posMinimax(M_minimax2)
print('(',a,',', b,')')
print('(',c,',', d,')')

# Exercice 2.2 (Maximum gap)
def getGap(L):
    return (getMax(L) - getMin(L))

def maxgap(M):
    maxGap = getGap(M[0])
    for i in range (1, len(M)):
        currGap = getGap(M[i])
        if currGap > maxGap:
            maxGap = currGap
    return maxGap

# Exercice 2.3 (Recherche)
# Ecrire la fonction qui recherche la position(x, y) d'un element e dans une matrice M

def searchMatrix(M, e):
    res, i, c, l = (-1, -1), 0, len(M[0]), len(M)

    while i < l and res == (-1, -1):
        j = 0
        while j < c and M[i][j] != e:
            j += 1
        if j < c:
            res = (i, j)
        i += 1

    return res

    
# Exercice 2.4 (Symétrique)
# Ecrire la fonction qui teste si une matrice carrée non vide est symmétrique
""" def _are_list_equals(L1, L2):
    l, i = 0, len(L1)
    while i < l and L1[i] == L2[i]:       TO BE RE-IMPLEMENTED
        i += 1
    if i < l-1:
        return False
    return True """

def symmetric(M):
    le, le0 = len(M), len(M[0])
    if le != le0:
        raise Exception("The dimensions are not correct")

#def _are_list_equals(L1, L2):
#def symmetric(M):



def SumColumn(A,j):
    n = len(A)
    s = 0
    for i in range(n):
        s += A[i][j]
    return s

def SumDiags(A):
    n = len(A)
    (s1, s2) = (0, 0)
    for i in range(n):
        s2 += A[i][i]
        s2 += A[i][n-i-2]
    return (s1, s2)

# Pers func
def SumLine(L):
    if L == []:
        return 0
    sum = 0
    for i in L:
        sum += i
    return sum

def magic_square(A):
    n = len(A)
    if n != len(A[0]):
        raise Exception("Not a square matrix")
    
    (diag_1, diag_2) = SumDiags(A)
    checker, i = (diag_1 == diag_2), 0

    while i < n and checker:
        checker = (diag_1 == SumLine(A[i]) and diag_1 == SumColumn(A, i))
        i += 1
    return checker

def list_nsq(n):
    l = []
    for i in range(n*n):
        l.append(False)
        n -= 1
    return l

def is_normal(A):
    i, j, n, checker = 0, 0, len(A), True
    L, n2 = list_nsq(n), n*n
    while i < n and checker:
        j = 0
        while j < n and checker: 
            if A[i][j] <= 0 or A > n2 or L[A[i][j]]:
                checker = False
            else:
                L[A[i][j]] = True
            j += 1
        j += 1
    return checker

def Siamise(n):
    S = classiques.initmatrix(n, n, 0)
    i = n - 1
    j = n // 2
    S[i][j] = 1

    for val in range(2, n*n + 1):
        # i, j ????
        i2 = (i + 1) % n
        j2 = (j + 1) % n
        if S[i2][j2] != 0:
            i -= 1
            if i == 0:
                i = n - 1
        else:
            (i, j) = (i2, j2)
        
        S[i][j] = val
    return S


#Harry Potter

