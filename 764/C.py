import math
for _ in range(int(input())):
    n = int(input())
    numbers = list(map(int, input().split(' ')))

    for i in range(n):
        numbers = sorted(numbers)
        numbers[-1] = int(math.floor(numbers[-1]/2))

    numbers = sorted(numbers)
    flag = False
    for i in range(1, len(numbers)):
        if numbers[i-1]+1 != numbers[i]:
            flag = True

    if flag:
        print('NO')
    else:
        print('YES')
