for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(a, reverse=True)
    alice = 0
    bob = 0

    for i in range(n):
        if alice <= bob:
            alice += a[i]
        else:
            bob += a[i]

    if alice == bob:
        print("YES")
    else:
        print("NO")
