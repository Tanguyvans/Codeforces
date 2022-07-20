import math
for _ in range(int(input())):
    n = int(input())
    elements = list(map(int, input().split(' ')))
    if n == 3:
        if elements[1] % 2 != 0:
            val = -1
            print(val)
        else:
            somme = sum(elements[1:-1])
            print(somme//2)
    else:
        somme = sum(elements[1:-1])
        if somme == len(elements[1:-1]):
            print('-1')
            continue

        odds = 0
        for i in elements[1:-1]:
            if i % 2 != 0:
                odds += 1

        if somme % 2 == 0:
            sol = int(somme/2 + odds/2)
            print(sol)

        else:
            sol = int(math.ceil(somme/2) + (odds-1)/2)
            print(sol)
