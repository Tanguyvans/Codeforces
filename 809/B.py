for _ in range(int(input())):
    n = int(input())

    numbers = dict()
    c = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if c[i] not in numbers:
            numbers[c[i]] = [1, i]
        else:
            last_i = numbers[c[i]][1]
            if last_i == 1 or last_i % 2 == 0:
                numbers[c[i]][0] += 1
                numbers[c[i]][1] = i
                ans = max(ans, numbers[c[i]][0])

    print(ans)
