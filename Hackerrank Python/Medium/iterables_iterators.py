from itertools import combinations
n = input()
l = input().split(" ")
m = int(input())
count = 0
for i in combinations(l, m):
    if 'a' in i:
        count += 1
print(count/len(list(combinations(l, m))))
