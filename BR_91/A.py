n = int(input())
imp = True
for i in [4, 7, 47, 74, 444, 447, 474, 477, 744, 747, 774, 777]:
    if n/i == int(n/i):
        imp = False

if imp:
    print('NO')
else:
    print('YES')
