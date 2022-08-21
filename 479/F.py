n = int(input())
a = list(map(int, input().split()))

d = {}

ans = 1
sol = [1]
for i in range(n):
    if a[i] not in d:
        if a[i] - 1 not in d:
            d[a[i]] = [i+1]
        else:
            mid = d[a[i]-1]
            mid.append(i+1)
            d[a[i]] = mid

            if len(mid) >= ans:
                ans = len(mid)
                sol = d[a[i]]

    elif a[i]-1 in d:
        mid = d[a[i]-1]
        mid.append(i+1)
        d[a[i]] = d[a[i]]

        if len(mid) >= ans:
            ans = len(mid)
            sol = d[a[i]]


print(ans)
print(*sol)
