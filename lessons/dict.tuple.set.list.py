# list упорядоченные изменяемые коллекции (список)
numbers = [1, 2, 3, 4, 5]         # список чисел
cars = ["BMW", "AUDI", "Tesla"]   # список строк
mixed = [10, "text", True, 3.14]  # комбинированный список
empty = []                        # пустой список

print(numbers[1])       # 2
print(cars[0])          # BMW
print(mixed[2])         # True

cars.append("Mercedes")        # добавляет новый элемент в конец списка
print(cars)                    # ['BMW', 'AUDI', 'Tesla', 'Mercedes']

cars.remove("AUDI")               # ['BMW', 'Tesla']
print(cars)                       # удвляет элемент

cars.insert(1, "Mercedes")     # добавляет в определенное место
print(cars)                    # ['BMW', 'Mercedes', 'Tesla']

cars.sort()                       # сортирует по алфавиту
print(cars)

# Tuple  упорядоченные не изменяемые коллекции (кортеж)
numbers = (1, 2, 3, 4, 5)         # кортеж чисел
cars = ("BMW", "AUDI", "Tesla")   # кортеж строк
mixed = (10, "text", True, 3.14)  # кортеж с разными типами данных

nums = (2, 3, 5, 8, 5, 9, 5)      
print(nums.count(5))           # считает сколько раз встречается число
print(nums.index(9))           # считает под каким индексом число


#set не упорядоченная коллекция, индекс не сохраняется
numbers = {1, 2, 3, 4, 5}     # множество чисел
fruts = {"apple", "banana"}   # множество строк

fruts.add("cherry")
print(fruts)


# dict не упорядоченные коллекции , хранит в виде пар ключ: значение(словарь)
person = {"name":"Yara", 'age':"25", "city":"Soligorsk"}   #создаем словарь с ключами и значениями
person ["profesiya"] = "IT"               # добавляем новую пару - ключ
print(person["profesiya"])
print(person.get('name'))                 # выводит значение по ключу (ищет во всем словаре)
print(person["name"])                     # выводит значение по ключу name
print(person["age"])                      # выводит значение по ключу age
