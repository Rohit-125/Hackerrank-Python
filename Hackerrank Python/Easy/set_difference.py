eng = int(input())
eng_roll = set(map(int, input().split()))

french = int(input())
french_roll = set(map(int, input().split()))

print(len(eng_roll.difference(french_roll)))
