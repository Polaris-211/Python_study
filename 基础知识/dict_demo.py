#字典dict key:value（键值对）
#my_dict = {key1: value1, key2: value2}
from email import message

name_dict = {"张三": 81, "李四": 82, "王五": 83}
none_dict = dict()

print(name_dict, type(name_dict))
print(none_dict)
#不允许重复
name_dict = {"张三": 81, "张三": 82, "王五": 83}
print(name_dict)

#通过[key]获取数据
name_dict = {"张三": 81, "李四": 82, "王五": 83}
score = name_dict["张三"]
print(score)

#字典的嵌套（key不可为字典）
stu_score_dict = {
    "张三":{
        "语文": 91,
        "数学": 92,
        "英语": 93
    },
    "李四":{
        "语文": 81,
        "数学": 82,
        "英语": 83
    },
    "王五":{
        "语文": 71,
        "数学": 72,
        "英语": 73
    }
}
print(stu_score_dict)
score = stu_score_dict["张三"]["语文"]
print(score)

#新增元素
name_dict["赵六"] = 84
print(name_dict)

#更新元素
name_dict["赵六"] = 94
print(name_dict)

#取出元素并在字典中删除pop
name_dict = {"张三": 81, "李四": 82, "王五": 83, "赵六":84}
value = name_dict.pop("李四")
print(value)
print(name_dict)

#清空元素clear
name_dict.clear()
print(name_dict)

#获取全部keys
name_dict = {"张三": 81, "李四": 82, "王五": 83, "赵六":84}
keys = name_dict.keys()
print(keys, type(keys))

#keys遍历字典for
for key in keys:
    print(key)
    print(name_dict[key])

#直接for
for key in name_dict:
    print(key)
    print(name_dict[key])

#统计元素数量len
length = len(name_dict)
print(length)

message_dict = {
    "王力鸿": {
        "部门": "科技部",
        "工资": 3000,
        "级别": 1
    },
    "周杰轮": {
        "部门": "市场部",
        "工资": 5000,
        "级别": 2
    },
    "林俊节": {
        "部门": "市场部",
        "工资": 7000,
        "级别": "3"
    },
    "张学油": {
        "部门": "科技部",
        "工资": 4000,
        "级别": 1
    },
    "刘德滑": {
        "部门": "市场部",
        "工资": 6000,
        "级别": 2
    }
}
print(message_dict)

for key in message_dict:
    if message_dict[key]["级别"] == 1:
        message_dict[key]["级别"] +=1
        message_dict[key]["工资"] += 1000
print(message_dict)


#容器间转换
list()
tuple()
str()
set()
dict()

#容器元素排序（都变成列表对象）
num_list = [1,3,4,2,5]
#正向排序
print(sorted(name_dict))
#反向排序
print(sorted(name_dict, reverse = True))

#确定最大最小值
print(max(num_list))
print(min(num_list))

print("b" > "ad")