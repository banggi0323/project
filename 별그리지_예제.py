#계단 (왼쪽 정렬)

n = int(input("정수 입력: "))
for i in range(1, n + 1):
    print("*"*i)

#계단 (오른쪽 정렬)

n = int(input("정수 입력: "))
for i in range(1, n + 1):
    print(" "*(n-i), "*"*i)

#거꾸로 계단 (왼쪽 정렬)

n = int(input("정수 입력: "))
for i in range(n, 0, -1):
    print("*"*i)

#거꾸로 계단 (오른쪽 정렬)

n = int(input("정수 입력: "))
for i in range(n, 0, -1):
    print(" "*(n-i) + "*"*i)

#세모모양

n = int(input("정수 입력: "))
for i in range(1, n+1):
    print(" "*(n-i) + "*"*(i*2-1))

#거꾸로 세모모양

n = int(input("정수 입력: "))
for i in range(n, 0, -1):
    print(" "*(n-i) + "*"*(i*2-1))

#마름모모양
n = int(input("정수 입력: "))
for i in range(1, n+1, 2):
    print(" "*((n-i)//2) + "*"*i)
for j in range(n-2, 0, -2):
    print(" "*((n-j)//2) + "*"*j)

#리본모양

n = int(input("정수 입력: "))
for i in range(1, n+1, 2):
    print("*"*(i//2+1) + " "*(n-i) + "*"*(i//2+1))
for j in range(n-2, 0, -2):
    print("*"*(j//2+1) + " "*(n-j) + "*"*(j//2+1))

#모래시계 모양

n = int(input("정수 입력: "))
for i in range(n, 0, -2):
    print(" "*((n-i)//2) + "*"*i)
for j in range(3, n+1, 2):
    print(" "*((n-j)//2) + "*"*j)


#트리플 삼각형모양

n = int(input("정수 입력: "))
for i in range(2, n+1,2):
    print(" "*(n-(i//2)) + "*"*(i-1))
for j in range(1, n+1, 2):
    print(" "*((n-j)//2) + "*"*j + " "*(n-j) + "*"*j)
