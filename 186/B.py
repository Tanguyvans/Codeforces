a = input()

sol = [0 for i in range(len(a))]
for i in range(1, len(a)):
    sol[i] = sol[i-1] + 1 if a[i-1] == a[i] else sol[i-1]

n = int(input())
for i in range(n):
    l, r = map(int, input().split())

    print(sol[r-1]-sol[l-1])
