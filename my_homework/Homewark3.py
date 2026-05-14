a = int(input())
b = int(input())
c = int(input())
print(a + b + c)
print(a - b - c)
print(a * b * c)
print(a - b + c)
print((a * b) / c)
print((a + b) % c)  # remainder = 0


cat_a = 6
cat_b = 4
print("Площадь", cat_a * cat_b / 2)
fdg = (cat_a**2 + cat_b**2) ** 0.5
print("Гипотенуза", fdg)


some_str1 = ("Hello world", "a b c", "test", "test1 test2 test3 test4 test5")
print(len(some_str1))
text = some_str1[3]
some_words = len(text.split())
print(some_words)


s = "hhhabchghhh"

first_h = s.find("h")
last_h = s.rfind("h")

result = s[: first_h + 1] + s[first_h + 1 : last_h].replace("h", "H") + s[last_h:]
print(result)


some_str3 = "qwertyuiop"
print(some_str3[2])
print(some_str3[-2])
print(some_str3[:5])
print(some_str3[:-2])
print(some_str3[::2])
print(some_str3[1::2])
print(some_str3[::-1])
print(some_str3[::-2])
print(len(some_str3))

some_str4 = "Hello"
print(some_str4[2])
print(some_str4[:5])
print(some_str4[:3])
print(some_str4[::2])
print(some_str4[1::2])
print(some_str4[::-1])
print(some_str4[::-2])
print(len(some_str4))


some_str5 = "TEST-STR"
print(some_str5[5])
print(some_str5[0])
print(some_str5[:5])
print(some_str5[:6])
print(some_str5[::2])
print(some_str5[1::2])
print(some_str5[::-1])
print(some_str5[::-2])
print(len(some_str5))

some_str6 = str(200)
print(200 % 10)

some_str7 = 123
result = (some_str7 // 10) % 10
print(result)

some_str8 = 123
line = some_str8 // 100
print(line)
line2 = (some_str8 // 10) % 10.0
print(line2)
line3 = some_str8 % 10
print(line3)
print(line + line2 + line3)
