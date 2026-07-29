#元组tuple（不可修改）

t1 = (1, "waibibabu", True)
t2 = ()
t3 = tuple()
print(t1)
t4 = ("hello")
print(t4, type(t4))

t5 = (("waibibabu"), (1, 2, 3))
print(t5, type(t5[1]))

#index查找
t6 = ("bibilabu", "wodedaodun", "bababoyi")
index = t6.index("bababoyi")
print(index)

#count统计
t7 = ("bibilabu", "wodedaodun", "bababoyi", "wodedaodun", "wodedaodun")
count = t7.count("wodedaodun")
print(count)

#len计算长度
length = len(t7)
print(length)

#while遍历
# index = 0
# while index < length:
#     print(t7[index])
#     index += 1

#for循环遍历
# for element in t7:
#     print(element)

#tuple中的list可改
t9 = (1, 2, 3, [4, 5, 6])
t9[3][0] =8
print(t9)


