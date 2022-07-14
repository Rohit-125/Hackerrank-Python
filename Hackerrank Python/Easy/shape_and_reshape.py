import numpy as np
l = list(map(int, input().split()))
arr = np.array(l)
arr.shape = (3, 3)
print(arr)
