a = int(input())
b = int(input())

if a == 0:
    print(0)
elif a < 0 and b % 2 != 0:
    print(-1)
else:
    print(1)
