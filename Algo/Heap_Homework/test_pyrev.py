def testing(L):
    L_return = []
    for i in reversed(range(len(L))):
        L_return.append(L[i])
    return L_return

Li = [0, 1, 2, 3, 4, 5]
print(testing(Li), '\n')

def _testing(L):
    L_return = []
    i = len(L) - 1
    while i >= 0:
        L_return.append(L[i])
        i -= 1
    return L_return
print(_testing(Li))
