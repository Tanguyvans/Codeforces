n = int(input())
a = input()
a = [i for i in a]
b = input()
b = [i for i in b]

ans = 0
for i in range(n):
    if a[i] != b[i]:
        if i < n-1 and a[i+1] == b[i] and a[i] == b[i+1]:
            mid = a[i]
            a[i] = a[i+1]
            a[i+1] = mid
            ans += 1
        else:
            ans += 1

print(ans)
