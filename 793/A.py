import math

for _ in range(int(input())):
    n = int(input())

    a = input()
    al = [i for i in a]

    start = a[int(math.floor(len(a)/2))]
    if n % 2 == 0:
        ans = 2
    else:
        ans = 1

    for i in range(int(math.floor(len(a)/2))+1, len(a)):
        if start == al[i]:
            ans += 2
        else:
            break

    print(ans)
