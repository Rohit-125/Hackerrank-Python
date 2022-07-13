import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    numpy_array = numpy.array(arr[::-1], float)
    return numpy_array

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
