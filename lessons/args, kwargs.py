def greet(*args):                    # args позволяет принимать любое количество позиционных аргументов
    print(args)                         # и превращает в кортежи
greet("dfgfdg", "sdfsdfg")

def greet(*names):
    for name in names:
        print(f"hello, {name}")
greet("алексей", "рома", "жора")




def user_info(**kwargs):                         # kwargs позволяет принимать любое количество именованных аргументов
    print(kwargs)                                  # и превращает в словарь
user_info(name="Yara", age=25, city="Sol")