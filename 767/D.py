from audioop import reverse


def isPalindrome(s):
    if s[0] == s[-1]:
        return True
    else:
        return False


for _ in range(int(input())):
    n = int(input())
    flag = False
    numbers = []

    ans = 0
    two_letters = set()
    three_letters = set()
    for i in range(n):
        s = input()

        if ans:
            continue
        if isPalindrome(s):
            ans = 1
            continue

        reverseS = s[::-1]

        if len(s) == 2:
            if reverseS in two_letters:
                ans = 1
                continue
            if reverseS in three_letters:
                ans = 1
                continue
            two_letters.add(s)
        elif len(s) == 3:
            if reverseS in three_letters:
                ans = 1
                continue
            if reverseS[:2] in two_letters:
                ans = 1
                continue
            three_letters.add(s[:2])
            three_letters.add(s)

    if ans:
        print('YES')
    else:
        print('NO')
