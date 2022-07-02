from collections import defaultdict
d = defaultdict(list)
list1 = []
m, n = map(int, input().split())
for i in range(m):
    a = input()
    d[a].append(i+1)
for i in range(n):
    b = input()
    list1 = list1 + [b]
for i in list1:
    if i in d:
        print(' '.join(map(str, d[i])))
    else:
        print("-1")
