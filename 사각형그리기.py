x = int(input("가로 : "))
y = int(input("세로 : "))

for i in range(x):
    print("*", end = '')

print("")
for j in range(y-2):
    print("*", end= '')
    for z in range(x-2):
        print("*", end = '')
    print("*")

for i in range(x):
    print("*", end = '')
