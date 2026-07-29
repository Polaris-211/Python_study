#集合set（不支持重复元素，无序，允许修改）

num_set = {1, 2, 3, 4, 5, 6, 1, 2, 3}
none_set = set()
print(num_set)
name_set = {"bibilabu", "bababoyi", "wodedaodun"}

#添加元素add
name_set.add("waibibabu")
print(name_set)

#移除指定元素remove
name_set.remove("bababoyi")
print(name_set)

#去除随机元素并在集合中删除pop
name_set = {"bibilabu", "bababoyi", "wodedaodun", "waibibabu"}
element = name_set.pop()
print(element)
print(name_set)

#清空集合clear
name_set.clear()
print(name_set)

#取两集合差集（1有2没有），产生新集合保持原集合不变difference
num_set1 = {1, 2, 3}
num_set2 = {1, 5, 6}
num_set3 = num_set1.difference(num_set2)
print(num_set1)
print(num_set2)
print(num_set3)

#消除差集，在集合1内部删除和集合二相同的元素，1变2不变difference_update
num_set1.difference_update(num_set2)
print(num_set1)
print(num_set2)

#合并两个集合union
num_set1 = {1, 2, 3}
num_set2 = {1, 5, 6}
num_set3 = num_set1.union(num_set2)
print(num_set1)
print(num_set2)
print(num_set3)

#统计集合数量len()
length = len(num_set)
print(length)

#集合的遍历for
for element in num_set:
    print(element)

my_list = ["黑马程序员", "传智教育", "黑马程序员", "传智教育", "itheima", "itcast", "itheima", "itcast", "best"]
my_set = set()
for element in my_list:
    my_set.add(element)
print(my_set)