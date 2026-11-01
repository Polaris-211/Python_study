"""
描述
2/1, 3/2, 5/3, 8/5, 13/8, …编写程序求出这个序列的前 n 项之和
"""
# n = int(input())
# sum = 0
# fz = [2]
# fm = [1]
# for i in range(n):
#     fz.append(fz[i] + fm[i])
#     fm.append(fz[i])
#     sum += fz[i] / fm[i]
# print(sum)
# str_ = input()
# _sum = 0
# for i in str_:
#     _sum += i
# print(_sum)

# n = int(input())
# ls = []
# while n > 0 :
#     ls.append(n % 2)
#     n = n // 2
# ls.reverse()
# print(''.join(map(str, ls)))

# n = int(input())
# _sum = 0
# for i in range(n):
#     _sum += 2**n
# print(_sum)
# for i in range(1, 15):
#     for j in range(1, 25):
#         if 7 * i + 4 * j == 100:
#             k = 100 - i - j
#             print(f"{i} {j} {k}")
# A = int(input())
# N = int(input())
# s = 0
# if 1<=A<=9 and 0<=N<=100000:
#     for i in range(N):
#         s += 
#         A = 10*A + A
#     print(s)
#     print(A)
# N = int(input())
# count = 0
# if 1 <= N <= 10000:
#     for i in range(1, N+1):
#         N3 = str(i**3)
#         pos = N3.rfind(str(i))
#         if pos == len(N3)-len(str(i)) :
#             print(i, end = " ")
#             count += 1
#     print(f'\n{count}')
# n = int(input())
# ls = []
# for i in range(n):
#     feet = int(input())
#     if feet%2 == 1:
#         print('0 0')
#     else:
       
#         for t in range(0, feet//4):
#             j = feet - 4*t
#             if j >= 0:
#                 ls.append(t + j)
#     print(f"{min(ls)} {max(ls)}")
# ls = list(map(int, input().split('\n')))
# import sys
# data = sys.stdin.read
# lso = []
# lsj = []
# for i in ls:
#     if i%2 == 0:
#         lso.append(i)
#     else:
#         lsj.append(i)
# print('-'.join(map(str, lso)))
# print('+'.join(map(str, lsj)))
# m = input()
# b = float(input())
# if m[-1] == '$':
#     z = float(m[:-1])*b
#     print(f"{z:.2f}￥")
# elif m[-1] == '￥':
#     z = float(m[:-1])/b
#     print(f"{z:.2f} $")
# else:
#     print('Data error!')
# print()
# dict1 = {
#         '赵广辉':'13299887777',
#         '特朗普':'814666888',
#         '普京':'522888666',
#         '吴京':'13999887777'}
# name = input()
# num = input()
# if name in dict1:
#     print('您输入的姓名在通讯录中已存在')
# else:
#     dict1[name] = num
#     print(dict1)

# goods=[
# {"name":"电脑","price":4999},
# {"name":"鼠标","price":80},
# {"name":"游艇","price":200000},
# {"name":"别墅","price":2000000},
# ]
# key = [i['name'] for i in goods]
# value = [i['price'] for i in goods]
# dict1 = dict(zip(key, value))
# print(dict1)
# goods=[
# {"name":"电脑","price":4999},
# {"name":"鼠标","price":80},
# {"name":"游艇","price":200000},
# {"name":"别墅","price":2000000},
# ]
# m = input()
# for i in goods:
#     print(f"{goods.index(i)} {i['name']}")
# for n in range(int(1000**(1/3)), int(999999**(1/4))+1):
#     str1 = str(n**3)
#     str2 = str(n**4)
#     if len(str1)==4 and len(str2)==6:
#         str0 = str1 + str2
#         for i in range(10):
#             if str0.count(str(i))!=1:
#                 break
#         else:
#             print(n)
#             break
nums = [0, 1, 0, 3, 12]
nums.sort(key=lambda x: x == 0)
print(nums)
