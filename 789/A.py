from collections import Counter

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split(' ')))

    b = Counter(a)

    if b[0]:
        print(len(a)-b[0])
    else:
        flag = False
        for v in b.values():
            if v > 1:
                flag = True

        if flag:
            print(len(a))
        else:
            print(len(a)+1)
