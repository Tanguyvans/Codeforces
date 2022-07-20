
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
word = input()
line = [i for i in word]

for i in line:
    if i.lower() not in vowels:
        print(f'.{i.lower()}', end='')
