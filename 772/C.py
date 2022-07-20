for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split(' ')))

    if a[-2] > a[-1] or len(a) == 1:
        print(-1)
        continue
    if a == sorted(a):
        print(0)
        continue

    nb_change = 0
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            nb_change += 1

    if nb_change > n:
        print(-1)
