import re
s = input()
pattern = r'([a-z A-Z 0-9])\1'
m = re.search(pattern, s)
if m:
    print(m.group()[0])
else:
    print(-1)
