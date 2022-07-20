n = int(input())
a = list(map(int, input().split()))

ans = 1
count = 0
sol = 1
prev = a[0]
p1 = 0
p2 = 0
for i in range(1, n):
    if prev >= a[i]:
        if count < 1:
            if i >= 2:
                if a[i-2] < a[i]:
                    count += 1
                    prev = a[i]
                    p2 = i
                else:
                    count = 1
                    ans = max(ans, sol)
                    sol = 1
                    p1 = i-1
                    p2 = i
                    prev = a[i]
            else:
                count += 1
                p2 = i
        else:
            count = 1
            ans = max(ans, sol)
            sol = i-p2
            p1 = p2
            p2 = i
            prev = a[i]

    else:
        prev = a[i]
        sol += 1

ans = max(ans, sol)

print(ans)
