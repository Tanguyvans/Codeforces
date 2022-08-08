msg = input()

upper = 0
lower = 0

for i in msg:
    if i == i.lower():
        lower += 1
    else:
        upper += 1

ans = min(upper, lower)
cst = 0
for i in msg:
    if i == i.lower():
        cst += 1
        lower -= 1
    else:
        upper -= 1

    ans = min(ans, cst+upper)

print(ans)
