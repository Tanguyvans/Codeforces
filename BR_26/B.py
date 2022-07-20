a = input()

l = 0
r = 0

for i in a:
    if i == '(':
        l += 1

    if i == ')' and l > r:
        r += 1

print(r*2)
