n = int(input())
a = list(map(int, input().split(' ')))
a = sorted(a)
m = int(input())
b = list(map(int, input().split(' ')))
b = sorted(b)

ans = 0
for i in range(len(a)):
    for j in range(len(b)):
        if b[j]-1 <= a[i] <= b[j]+1:
            ans += 1
            b.remove(b[j])
            break

print(ans)
