a = input()

if int(a) > 0:
    print(a)
else:
    a2 = a[:-2] + str(min(a[-2], a[-1]))
    print(int(a2))
