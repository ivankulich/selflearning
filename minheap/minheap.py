"""
Rearrange input list into min-heap and return it.
Elements are sored in list like this: for every item A[i] in list correct: A[i] ≤ A[2i + 1] and A[i] ≤ A[2i + 2].

Переставить элементы заданного массива чисел так, чтобы он удовлетворял свойству мин-кучи.
Вход. Массив чисел A[0 . . . n − 1].
Выход. Переставить элементы массива так, чтобы выполнялись неравенства A[i] ≤ A[2i + 1] и A[i] ≤ A[2i + 2] для всех i.

"""

def min_heap_from_list(lst):
    def shift_down(lst, pos):
        was_shiftodwn = False
        while True:
            leftChildIndex = pos * 2 + 1
            rightChildIndex = pos * 2 + 2
            minimalChildIndex = pos
            if leftChildIndex < len(lst) and lst[leftChildIndex] < lst[minimalChildIndex]:
                minimalChildIndex = leftChildIndex
            if rightChildIndex < len(lst) and lst[rightChildIndex] < lst[minimalChildIndex]:
                minimalChildIndex = rightChildIndex
            if minimalChildIndex == pos:
                return was_shiftodwn
            lst[pos], lst[minimalChildIndex] = lst[minimalChildIndex], lst[pos]
            was_shiftodwn = True
            pos = minimalChildIndex

    i = (len(lst) // 2) - 1
    while i >= 0:
        shift_down(lst, i)
        i -= 1
    return lst

# test data
# A = [3, 5, 8, 2, 9, 4, 1]
A = [3, 5, 8, 2, 9, 82, 56, 23, 4, 5, 16, 17, 56, 7]

print(min_heap_from_list(A))