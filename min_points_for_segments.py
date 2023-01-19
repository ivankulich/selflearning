"""
Жадные алгоритмы. Покрыть отрезки точками.

По данным n отрезкам необходимо найти множество точек минимального размера,
для которого каждый из отрезков содержит хотя бы одну из точек.
В первой строке дано число 1 ≤ n ≤100 отрезков.
Каждая из последующих n строк содержит по два числа 0 ≤ l ≤ r ≤ 10**9, задающих начало и конец отрезка.
Выведите оптимальное число m точек и сами m точек. Если таких множеств точек несколько,
выведите любое из них.
"""

n = int(input())

lst = [[] for _ in range(n)]

for k in range(n):
    lst[k].extend([int(i) for i in input().split()])

lst.sort(key=lambda right: right[1])

result = []
elem = lst[0]
result.append(elem[1])
lst.pop(0)


while len(lst) > 0:
    while len(lst) > 0 and lst[0][0] <= elem[1]:
        lst.pop(0)
    if len(lst) > 0:
        elem = lst[0]
        result.append(elem[1])
        lst.pop(0)


print(len(result))
print(*result)
