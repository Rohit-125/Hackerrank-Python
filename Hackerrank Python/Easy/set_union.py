EN = int(input())
english = set(map(int, input().split()))
FR = int(input())
french = set(map(int, input().split()))

print(len(english.union(french)))
