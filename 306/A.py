word = input()

letters = [i for i in word]

ab = []
ba = []

flag = False
for i in range(len(letters)-1):
    if letters[i] + letters[i+1] == 'AB':
        ab.append(i)

    if letters[i] + letters[i+1] == 'BA':
        ba.append(i)

for i in range(len(ab)):
    for j in range(len(ba)):
        if ab[i]+1 < ba[j] or ab[i]-1 > ba[j]:
            flag = True
            break


if flag:
    print('YES')
else:
    print('NO')
