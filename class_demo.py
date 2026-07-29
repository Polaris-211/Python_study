class Student: #设计类
    # name = None
    # gender = None
    # nationality = None
    # native_place = None
    # age = None #成员变量
#以上可以不写，下面的函数中直接定义
    def __init__(self, name, gender, nationality, native_place, age): #构造方法  自动执行
        self.name = name
        self.gender = gender
        self.nationality = nationality
        self.native_place = native_place
        self.age = age
        print("大家好")
    #
    # def say_hi(self):
    #     print(f"大家好， 我是{self.name}")#成员方法  调用self在成员方法中访问成员变量
    # def say_hello(self, sentence):
    #     print(f"hi, {sentence}")



#创建对象
stu_1=Student("张三", "男", "China", "安徽", 18)
print(stu_1) #输出地址
# stu_2=Student()
#
# #对象属性赋值
# stu_1.name = "张三"
# stu_1.gender = "男"
# stu_1.nationality = "China"
# stu_1.native_place = "安徽"
# stu_1.age = 18
#
# stu_2.name = "李四"
# stu_2.gender = "女"
# stu_2.nationality = "America"
# stu_2.native_place = "纽约"
# stu_2.age = 28
#
# print(stu_1.name)
# print(stu_1.nationality)
# print(stu_1.native_place)
# print(stu_1.age)
# print(stu_2.name)
# print(stu_2.nationality)
# print(stu_2.native_place)
# print(stu_2.age)
#
# stu_1.say_hi()
# stu_1.say_hello("大家好")

#
# class Students:
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address
#
# for num in range(1, 11):
#     print(f"当前录入第{num}个学生信息， 一共要录入10个")
#     stu = Students(input("请输入学生姓名"), input("请输入学生年龄"), input("请输入学生地址"))
#     print(f"第{num}个学生信息已录入，信息为：【学生姓名：{stu.name}，学生年龄：{stu.age}，学生地址：{stu.address}】")

#魔术方法
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self): #字符串魔术方法
        return f'Student类对象，name = {self.name}, age = {self.age}'

    def __lt__(self, other): #小于（大于）比较方法
        return self.age < other.age

    def __le__(self, other): #小于（大于）等于比较方法
        return self.age <= other.age

    def __eq__(self, other):  #等于比较方法
        return self.age == other.age


student1 = Student("张三", 20)
student2 = Student("李四", 20)
print(student1)
print(str(student1))
print(student1 > student2)
print(str(student1) <= str(student2))
print(student1 == student2)