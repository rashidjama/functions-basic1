# #1
# def a():
#     return 5
# print(a())
# I predicted 5 

#2
# def a():
#     return 5
# print(a()+a())
# I predicted 10

# #3
# def a():
#     return 5
#     return 10
# print(a())
# I predicted 5, any code after first return never get executed

# #4
# def a():
#     return 5
#     print(10)
# print(a())
# I predicted 5

#5
# def a():
#     print(5)
# x = a()
# print(x)
# I predicted 5 and none because didn't return explicitly anything

# #6
# def a(b,c):
#     print(b+c)
# print(a(1,2) + a(2,3))
# I predicted wrong this one but understand whey my result was different from computer

# #7
# def a(b,c):
#     return str(b)+str(c)
# print(a(2,5))
# I predicted 25 because strings are concadinated

# #8
# def a():
#     b = 100
#     print(b)
#     if b < 10:
#         return 5
#     else:
#         return 10
#     return 7
# print(a())
# I predicted 100 and 10

# #9
# def a(b,c):
#     if b<c:
#         return 7
#     else:
#         return 14
#     return 3
# print(a(2,3))
# print(a(5,3))
# print(a(2,3) + a(5,3))
# I predicted 7, 14, 21

# #10

# def a(b,c):
#     return b+c
#     return 10
# print(a(3,5))
# I predicted 8

# #11
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
# print(b)
# a()
# print(b)
# I predicted 500, 500, 300, 500

# #12
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return b
# print(b)
# a()
# print(b)
# I predicted 500, 500, 300, 500

# #13
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return b
# print(b)
# b=a()
# print(b)
# I predicted 500, 500, 300, 300

# #14
# def a():
#     print(1)
#     b()
#     print(2)
# def b():
#     print(3)
# a()
# I predicted 1, 3, 2

# #15
# def a():
#     print(1)
#     x = b()
#     print(x)
#     return 10
# def b():
#     print(3)
#     return 5
# y = a()
# print(y)
# I predicted 1 , 3, 5, 10
# copy
#  Create a text file, or copy the code snippets into a Python file
