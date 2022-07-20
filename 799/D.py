import math

for _ in range(int(input())):
    palindrome = 0
    time, k = map(str, input().split())
    k = int(k)
    h0, m0 = map(int, time.split(':'))

    if str(h0) == str(m0)[::-1]:
        palindrome += 1

    h = (h0+int(math.floor(k/60))) % 12
    m = (m0+k % 60) % 60
    while h != h0 or m != m0:
        sh = str(h)
        sm = str(m)

        if len(sh) == 1:
            sh = '0' + sh
        if len(sm) == 1:
            sm = '0' + sm

        if sh == sm[::-1]:
            palindrome += 1

        m = (m+k % 60)
        if m >= 60:
            h += 1
            m = m % 60
        h = (h+int(math.floor(k/60))) % 12

        print(h, m)

    print(palindrome)
