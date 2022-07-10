n = int(input())
s = set(map(int, input().split()))
for i in range(int(input())):
    enter = input()
    if enter == "pop":
        s.pop()
    else:
        command, value = enter.split()
        if command == "discard":
            s.discard(int(value))
        else:
            s.remove(int(value))
print(sum(s))
