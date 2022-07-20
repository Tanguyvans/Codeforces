from collections import Counter
import math

n = int(input())

boxes = list(map(int, input().split(' ')))
boxes = sorted(boxes, reverse=True)
c = Counter(boxes)

ans = int(c[100] + max(0, math.ceil((c[50]-c[100])/3)))

print(ans)
