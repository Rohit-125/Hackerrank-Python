from collections import namedtuple
n = int(input())
data = namedtuple("data", input())
print(sum([int(data(*input().split()).MARKS) for i in range(n)])/n)

# THE FOLLOWING CODE IS JUST TO REFER AND UNDERSTAND

# from collections import namedtuple
# n = int(input())
# data = namedtuple("data", imnput())
# marks_lst = []
# for i in range(n):
#       marks = int(data(*input().split()).MARKS)
#       marks_lst.append(marks)
# print(sum(marks_lst)/n)
