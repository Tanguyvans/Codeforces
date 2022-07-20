n = int(input())

for _ in range(n):
    n_numbers = int(input())
    line = list(map(int, input().split()))
    print(max(line)-min(line))
