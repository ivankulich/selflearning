"""
Первая строка содержит количество предметов 1≤n≤10**3 и вместимость рюкзака 0≤W≤2*10**6.
Каждая из следующих n строк задаёт стоимость 0≤c(i)≤2*10**6 и объём 0<w(i)≤2*10**6 предмета (n, W, c(i), w(i) — целые числа).

Выведите максимальную стоимость частей предметов (от каждого предмета можно отделить любую часть,
стоимость и объём при этом пропорционально уменьшатся), помещающихся в данный рюкзак,
с точностью не менее трёх знаков после запятой.
"""

n, W = [int(i) for i in input().split()]
# print(n, W)

lst = []
for _ in range(n):
    a, b = [int(i) for i in input().split()]
    c = a / b
    lst.append([a, b, c])

lst.sort(key = lambda x: x[2], reverse = True)
# print(lst)

result_m = 0
result_w = 0
for i in range(len(lst)):
    if W - result_w - lst[i][1] > 0:
        result_m += lst[i][0]
        result_w += lst[i][1]
    else:
        result_m += lst[i][0] * ((W - result_w) / lst[i][1])
        break

print(result_m)
