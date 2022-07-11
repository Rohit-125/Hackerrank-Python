from itertools import groupby

result = [(len(list(c)), int(k)) for k, c in groupby(input())]

print(*result)
