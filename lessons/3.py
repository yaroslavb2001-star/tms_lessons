a = 10
b = 7
print(a / b)
number: float = 0.7142857142857143
print(round(number, 2))
print(a // b)  #операция целочисленного деления
print(a**b)  #операция возведения в степень
print(a % b) # операция получения остатка
print(a==b)  # проверяет, равен ли левый операнд правому
print(a!=b) # проверяет неравенство левого операнда правому

a =  ["1" ,"2" ]
b =  ["1", "2" ]
     
print(a is b) #проверяет тождественное равенство – находятся ли два значения по одному адресу в памяти


some_str = "abracadabra"
print(some_str)
print(some_str[3], some_str[5])
print(some_str[1:3])
print(some_str[::3])
print(len(some_str))

some_str = "asdfghjk fgyu"
print(some_str.upper())  # все большие
print(some_str.capitalize())  # только первая большая
print(some_str.title())  # заглавные буквы большие
print(some_str.lower())  # из больших в маленькие



some_str: str = "sdfd"
print(some_str.isalpha()) # проверка слов

some_str: str = "123"
print(some_str.isdigit()) # проверка цифр

some_str: str = "123sdf"
print(some_str.isalnum()) # комбинированное

# складывание строк
some_str1= "str1"
some_str2="srt2"
result=f"{some_str1} {some_str2}"
print(result)

some_str = "123 asd 456 hya ghy"
print(some_str.find("y"))
print(some_str.rfind("y"))
print(some_str.count(""))
print(some_str.find("x"))
print(some_str.replace("123", "321"))

