n, m = map(int, input().split())
a = list(map(int, input().split()))

left = [0 for i in range(n)]
right = [0 for i in range(n)]
for i in range(1, n):
    left[i] = left[i-1] + a[i-1]-a[i] if a[i] < a[i-1] else left[i-1]

for i in range(n-2, -1, -1):
    right[i] = right[i+1] + a[i+1]-a[i] if a[i] < a[i+1] else right[i+1]

for i in range(m):
    s, t = map(int, input().split())
    if s < t:
        print(left[t-1] - left[s-1])
    else:
        print(right[t-1]-right[s-1])
