def my_add(a, b, c):
    print(a + b + c)


tuple1 = (1, 2, 3)
my_add(*tuple1)
list2 = [x * 2 for x in range(4, 7)]
my_add(*list2)
dict1 = dict(zip(list(range(3)), [x * 100 for x in range(3)]))
my_add(*dict1.values())
"""
6
30
300
"""
