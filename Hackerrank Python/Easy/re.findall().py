""" (?<=):- It matches if the current position in the string is preceded by a match for ... that ends at the current position. 
It's called positive lookbehind assertion. (?<=abc) def will back up 3 characters and check if the contained pattern matches. """

import re
s = input()
v = "aeiou"
c = "qwrtypsdfghjklzxcvbnm"
l = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (c, v, c), s, flags = re.IGNORECASE)

if not l:
    print(-1)
else:
    for i in l:
        print(i)
