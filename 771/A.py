for _ in range(int(input())):
    n = int(input())
    numbers = list(map(int, input().split(' ')))

    inter = 1
    a = -1
    b = -1
    for i, nb in enumerate(numbers):
        if nb == inter:
            inter += 1
            continue
        else:
            a = i
            b = numbers.index(inter)
            break

    if a == b == -1:
        print(*numbers)
    else:
        numbers[a:b+1] = reversed(numbers[a:b+1])
        print(*numbers)
