#
#
#1
# a = int(input("Введите число: "))
# k = 0
# for i in range(2, a // 2+1):
#     if (a % i == 0):
#         k = k+1
# if (k <= 0):
#     print("Число простое")
# else:
#     print("Число не является простым")
#2
# a = [9,8,7,6,5,4,3,2,1]
# b = 1
# while b < len(a):
#      for i in range(len(a)-b):
#           if a[i] > a[i+1]:
#                a[i],a[i+1] = a[i+1],a[i]
#      b += 1
# print(a)
#3
# def search_bnum(cur):
#     most = cur[0]
#     for i in range(1, len(cur)):
#      if cur[i] > most:
#       most = cur[i]
#     return most
# list = [1,2,3,4,5,6,7,8,9,10]
# mostel = search_bnum(list)
# print(mostel)
#4
# def phib(a):
#     if a == 1 or a == 2:
#         return 1
#     return phib(a - 1) + phib(a - 2)
# b = int(input())
# print(phib(b))
# #5
# s= ['tshhs','stdhsth','tshhs']
# c=0
# a=0
# for i in s:
#   if s.count(i)>=c:
#    c=s.count(i)
# a=i
# print(a)