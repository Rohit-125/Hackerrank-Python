k = int(input())
lst = list(map(int, input().split()))

s1 = set() # unique room no list
s2 = set() # room no. appearing more than once

for i in lst:
    if i in s1:
        s2.add(i)
    else:
        s1.add(i)
        
s = s1.difference(s2)
print(*s)
