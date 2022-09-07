from collections import Counter

for _ in range(int(input())):
    a, b = list(input())
    c, d = list(input())

    l = [a, b, c, d]

    sol = Counter(l)

    print(len(sol)-1)
