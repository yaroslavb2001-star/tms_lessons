def say_hello(name):
    print("Hello", name)

say_hello("Mariya")
say_hello("Yaroslav")


def make_gretting(name):
    return "hello "  + name

result = make_gretting("oleg")
print(result)
result = make_gretting("Yara")
print(result)



# def add (a, b):
#     print(a + b) #просто выведет значение 


def add(a, b):
    return a + b # можно переписывать много раз

result = add(5, 6)*2
print(result)
result = add(7, 8) / 6
print(result)