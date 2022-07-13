import re

pattern = r"(?<= )(&&|\|\|)(?= )"
replacement = lambda x: "and" if x.group() == "&&" else "or"

for i in range(int(input())):
    s = input()
    print(re.sub(pattern, replacement, s))
