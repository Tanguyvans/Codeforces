n = int(input())

if n == 1:
    print(0)
elif n == 2:
    print(3)
elif n == 3:
    print(6)
else:
    n1 = 3
    n2 = 6

    for i in range(3, n):
        a = (n1 * 3 + n2*2) % 1000000007

        n1 = n2
        n2 = a

    print(a)
