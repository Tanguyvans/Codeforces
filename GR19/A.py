for _ in range(int(input())):
    n = int(input())

    numbers = list(map(int, input().split(' ')))
    sorted_numbers = sorted(numbers)
    if numbers == sorted_numbers:
        print('NO')
    else:
        print('YES')
