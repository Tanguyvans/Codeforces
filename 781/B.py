for _ in range(int(input())):
    n = int(input())

    numbers = list(map(int, input().split(' ')))
    len_nb = len(numbers)

    nb_dict = dict()
    for nb in numbers:
        if nb in nb_dict:
            nb_dict[nb] += 1
        else:
            nb_dict[nb] = 1

    max_val = max(nb_dict.values())

    ans = n-max_val

    while max_val < n:
        ans += 1
        max_val *= 2

    print(ans)
