n = int(input())
a = input()
a = [int(i) for i in a]

s = {0: [], 1: [], 2: [2], 3: [3], 4: [3, 2, 2], 5: [5], 6: [
    5, 3], 7: [7], 8: [7, 2, 2, 2], 9: [7, 3, 3, 2]}

ans = []
for ai in a:
    ans.extend(s[ai])

ans = sorted(ans, reverse=True)

for i in ans:
    print(i, end='')
