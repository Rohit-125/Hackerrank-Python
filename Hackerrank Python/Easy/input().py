xk = list(map(int, input().split()))
x = xk[0]
k = xk[1]
P = input()
if eval(P) == k:
    print(True)
else:
    print(False)
