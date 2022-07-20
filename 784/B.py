from collections import Counter

for _ in range(int(input())):

    n = int(input())

    if n < 3:
        input()
        print(-1)
    else:
        nb = list(map(int, input().split(' ')))

        cnt = Counter(nb)

        flag = True
        for k, v in cnt.items():
            if v >= 3:
                print(k)
                flag = False
                break

        if flag:
            print(-1)
