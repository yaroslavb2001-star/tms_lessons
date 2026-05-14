try:
    x = int(input("введите число:"))
    print(10 / x)
except:                                    # выводит "произошла ошибка" без самой ошибки
    print("произошла ошибка")

try:
    x = int(input("введите число: "))
    print(10 / x)
except ValueError:                       # первое находит определенную ошибку(если ввели буквы а не цифры), а дальше все остальные
    print("это не число")
except:
    print("произошла ошибка")

try:
    x = int(input("введите число: "))
    print(10 / x)
except Exception as e:                 # ищет все возможные ошибки
    print("ошибка:", e)


try:
    x = int(input("введите число:"))
    print(10 / x)
except ValueError:
    print("ошибка ввода")
else:                                     # else выполняет тогда когда код в try отработал без ошибок, т.е. ввели число
    print("ты ввел:", x)


try:
    x = int(input("число:"))
    print(10 / x)
except:
    print("ошибка")
finally:                                    # finally происходит в любом случае
    print("программа завершена")