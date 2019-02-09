# numbers=[1,2,3,4,5,6]
# def square (x):
#     return x**2
# print(list(map(square,numbers)))
# print(list(map(lambda x: x**2, numbers)))

# def greater_than_three(x):
#      return x>3
# print(list(filter(lambda x: x>3,numbers)))

from functools import reduce
numbers=[1,2,3,4,5]
print(reduce(lambda x,y: x*y ,numbers))
