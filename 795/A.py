
for _ in range(int(input())):
    odd = 0
    even = 0

    n = int(input())
    a = list(map(int, input().split(' ')))

    for i in range(n):
        if a[i] % 2 == 0:
            even += 1
        else:
            odd += 1

    print(min(odd, even))
