from login_heaps import *
from random import randint


def test_creation():
    assert (Heap() == [None])


def test_isempty():
    H = [None]
    assert (is_empty(H))
    H = [None, (1, None)]
    assert (not is_empty(H))


def test_push():
    H = [None, (2, 'A'), (12, 'C'), (10, 'B'), (24, 'I'), (16, 'E'), (14, 'D'), (18, 'F'), (30, 'L'), (26, 'J'),
         (20, 'G'), (32, 'M'), (28, 'K'), (22, 'H')]
    push(H, 'N', 5)
    assert (H == [None, (2, 'A'), (12, 'C'), (5, 'N'), (24, 'I'), (16, 'E'), (14, 'D'), (10, 'B'), (30, 'L'), (26, 'J'),
                  (20, 'G'), (32, 'M'), (28, 'K'), (22, 'H'), (18, 'F')])


def test_pop():
    H = [None, (2, 'A'), (12, 'C'), (5, 'N'), (24, 'I'), (16, 'E'), (14, 'D'), (10, 'B'), (30, 'L'), (26, 'J'),
         (20, 'G'), (32, 'M'), (28, 'K'), (22, 'H'), (18, 'F')]
    assert (pop(H) == (2, 'A'))
    assert (H == [None, (5, 'N'), (12, 'C'), (10, 'B'), (24, 'I'), (16, 'E'), (14, 'D'), (18, 'F'), (30, 'L'),
                  (26, 'J'), (20, 'G'), (32, 'M'), (28, 'K'), (22, 'H')])


def test_isheap():
    T = [None, 2, 12, 10, 24, 16, 14, 18, 30, 26, 20, 32, 28, 22]
    assert (is_heap(T))
    T = [None, 12, 2, 24, 19]
    assert (not is_heap(T))


def is_sorted(L):
    i = 1
    b = True
    while i < len(L) and b:
        b = L[i][1] >= L[i - 1][1]
        i += 1
    return b


def generate_random(length):
    L = []
    for i in range(length):
        L.append((None, randint(0, 100)))
    return L


def test_is_sorted():
    assert (is_sorted([(None, 1), (None, 2), (None, 3), (None, 10), (None, 200)]))
    assert (not is_sorted([(None, 2), (None, 1), (None, 10), (None, 3), (None, 200)]))


def test_heap_sort():
    assert (is_sorted(heap_sort(generate_random(100))))
    L = [('A', 20), ('B', 5), ('C', 10), ('D', 12), ('E', 15), ('F', 8), ('G', 2), ('H', 6), ('I', 2), ('J', 9)]
    assert (heap_sort(L) == [('G', 2), ('I', 2), ('B', 5), ('H', 6), ('F', 8), ('J', 9), ('C', 10), ('D', 12),
                             ('E', 15), ('A', 20)])