name_list = ["bibilabu", "bababoyi", "wodedaodun"]
num_list = [[1,2,3],[4,5,6],[7,8,9]]

# print(num_list[0][-1])
# print(num_list[1][-2])
# print(num_list[2][-3])
# print(name_list[0])
# print(name_list[1])
# print(name_list[2])

#获取下标
index = name_list.index("bababoyi")
print(index)

#插入元素
name_list.insert(-1,"waibibabu")
print(name_list)

#插入到末尾
name_list.append("bagayalun")
print(name_list)

#将一个数据容器插入到尾部
name_list.extend(num_list)
print(name_list)

name_list = ["bibilabu", "bababoyi", "wodedaodun"]
#del指定下标删除
del name_list[1]
print(name_list)

#pop删除并得到返回值
element = name_list.pop(0)
print(name_list)
print(element)

name_list = ["bibilabu", "bababoyi", "wodedaodun","bababoyui"]
#删除某元素在列表中的第一个匹配项
name_list.remove("bababoyi")
print(name_list)

#清空列表
num_list[2].clear()
print(num_list)

#统计元素个数
name_list = ["bibilabu", "bababoyi", "wodedaodun","bababoyi"]
cont = name_list.count("bababoyi")
print(cont)

#列表中元素数量
length = len(num_list[0])
print(length)


num_list = [21, 25, 21, 23, 22, 20]
num_list.append(31)
print(num_list)

num_list.extend([29, 33, 30])
print(num_list)

first_element = num_list.pop(0)
print(first_element)

last_element = num_list.pop(-1)
print(last_element)

index = num_list.index(31)
print(index)



