for _ in range(int(input())):
    n = int(input())
    numbers = list(map(int, input().split(' ')))
    cnt = 0
    mx = 0
    for i, nb in enumerate(numbers):
        mx = max(mx, nb)
        if mx == i+1:
            cnt += 1
    print(cnt)
