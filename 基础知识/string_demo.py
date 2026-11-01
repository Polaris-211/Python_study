#字符串string（无法修改）
from idlelib.replace import replace

#格式化输出
"{}{}".format()

str1 = "bibilabu and wodedaodun"
value = str1[-4]
print(value, type(value))
print(str1)

#字符串的查找
index = str1.index("and")
print(index, type(index))
str1.rindex() #返回最后一次出现位置

#字符串的替换replace
new_str = str1.replace("bi", "wai")
print(new_str)

#字符串分割成列表split
str2 = "Hello the great world"
new_str2 = str2.split(" ")
print(new_str2)

#清楚头尾空格/指定参数strip
str3 = "  Hello the great world   "
new_str3 = str3.strip()
print(new_str3)

str4 = "12Hello the great world321"
new_str4 = str4.strip("12")
print(str4, new_str4)

#统计字符串某字符出现的次数count
str1 = "bibilabu and wodedaodun"
count = str1.count("bi")
print(count)

#统计字符串长度
length = len(str1)
print(length)

#序列切片：从一个序列中取子序列
#序列[起始（留空即开头）:结尾（不含）（留空即末尾）:步长（为负即取反）]
str5 = "1234567"
new_str5 = str5[3:1:-1]
print(new_str5)

str6 = "万过薪月，员序程码黑来，nohtyp来"
index1 = str6.index("黑")
index2 = str6.index("员")-1
new_str6 = str6[index1:index2:-1]
print(new_str6)

str7 = "万过薪月，员序程码黑来，nohtyp来"
new_str7 = str7.split("，")[1].replace("来", "")[::-1]
print(new_str7)
# new_str9 = new_str8.replace("来", " ")
# new_str10 = new_str9[:-1]
