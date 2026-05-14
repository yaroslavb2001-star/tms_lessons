add = lambda a,b: a + b   # lambda
print(add(5,6))

res = lambda x: x % 2 ==0
print(res(8))
print(res(7))


numbers = [1, 2, 3, 4, 5, 6]        # map
def add (b):
    return b + b
res = list(map(add, numbers))       # add = lambda b: b + b
print(res)

numbers = [1, 2, 3, 4, 5, 6]  
print(list(map(lambda b: b + b, numbers)))       # add = lambda b: b + b (сократили формулу)


# map принимает функцию к каждому элементу отдельно (функция, последовательность)
names = ["alexey", "yaroslav", "danik"]
print(list(map(lambda x: x.upper(),names)))        # map для списка

# filter отбирает элементы по условию (функция, последовательность)             
numbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]          
print(list(filter(lambda x: x % 2 ==0, numbers)))   # filter

# reduce объеденяет все элементы в один результат (функция, последовательность)
from functools import reduce
numbers = [1, 2, 3, 4]
print(reduce(lambda a,b: a + b, numbers))
