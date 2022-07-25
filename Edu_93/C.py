for _ in range(int(input())):
    n = int(input())
    a = input()

    b = [0]

    for i in range(n):
        b.append(b[i]+int(a[i]))

    print(b)
