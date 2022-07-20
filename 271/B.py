n = int(input())
a = list(map(int, input().split(' ')))

a0 = 0
aa = [0 for i in range(n)]
for i in range(n):
    aa[i] = a0 + a[i]
    a0 = aa[i]

m = int(input())
b = list(map(int, input().split(' ')))

for bi in b:
    l = 0
    u = n
    while l < u:
        inter = (l+u)//2

        if aa[inter] >= bi:
            u = inter
        else:
            l = inter + 1

    print(u+1)
