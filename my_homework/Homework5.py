from math import  radians, factorial



x = radians(360)
n = 5
d_sin = x - x**3 / factorial(3) + x**5 / factorial(5) - x**7 / factorial(7) + ((-1)**n) * (x**(2*n + 1)) / factorial(2*n+1)
print(d_sin)


x = radians(180)
n = 4
d_cos = 1 - x**2 / factorial(2) + x**4 / factorial(4) - ((-1)**n) * (x**2*n / factorial(2 * n))
print(d_cos)

# №2
x = 3000  # стоимость телефона
k = 25  # откладывает каждый день кроме вскр

summa_n = 0
day = 0
while summa_n < 3000:

    summa_n += 25
    print(f"отложила {summa_n} рублей", end=", ")

    day += 1
    print(f"Нужно {day} дней")

week = 120 / 6
print(f"понадобится {week} недель, и {day} дней для покупки телефона")



# №3
a, b = 0, 1
for i in range(12):
    print(a, end=" ")
    a, b = b, a + b




# №4
some_list = [2, 4, 7, 8, 23, 56, 78, 78]
total = sum(some_list)
print(total)
min_number = min(some_list)
max_number = max(some_list)
print(f"минимальное значение {min_number}, максимальное значение {max_number}")




# №5
numbers = [1,   2,   3,  4,  5,]
if len(numbers) != len(set(numbers)):
    print("Есть повторяющиеся числа")
else:
    print(" Все числа уникальны")





# №6
def binary_search(spisok, item):
    left = 0
    right = len(spisok) - 1

    while left <= right:
        mid = (left + right) // 2
        guess = spisok[mid]
        if guess == item:
            return mid
        if guess > item:
            right = mid - 1
        else:
            left = mid + 1
    return None


my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
target = 80
result = binary_search(my_list, target)
print(f"Позиция элемента {target}: {result}")
