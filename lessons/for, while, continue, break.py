for i in range(5):                   # for
    print("hello")
    print(i)

    for i in range(1, 8, 2):
        print(i)

total = 0
for i in range(1, 7):
     total = total + i
print(total)


for i in range(5):
     for j in range(5):
          print(i, j)

for i in range(5):
    if i ==3:
        break               #break
    print(i)

for i in range(5):
        if i ==2:
            continue        #continue
        print(i)

for i in range(1, 15):
    if i % 9 == 0:
        print("good", i)
        break                       #break
    print("not good", i)

for i in range(1, 25):
    if i % 2 == 0:
        continue
    print("нечетное число", i)    #continue

i = 1
while i <= 10:                    # while
    print(i)
    i = i + 3

while True:
    command = input("введите значение:")
    if command == "stop":
        print("okey")
        break
    print("еще раз попробуй:", command)
