#函数多返回值
def test_return():
    return 1, "hello", True
x, y, z = test_return()
print(x, y, z)

#关键字传参
def user_info(name, age, gender):
    print(name, age, gender)
#可不按位置，也可位置和关键字混用（位置参数必须在前）
user_info("小明", gender =  "男", age = 21)

#缺省参数（不传参即用默认值,默认值必须在最后）
def user_info(name, age = 10, gender = "男"):
    print(name, age, gender)
user_info("小天")

#不定长参数/可变参数
#位置传递，args会合并为元组
def user_info(*args):
    print(args, type(args))
user_info(1, 2, 3)
#关键字传递,参数“键 = 值”，形成字典
def user_info(**kwargs):
    print(kwargs, type(kwargs))
user_info(name = "Tom", age = 18, gender = "男")

#函数作为参数调用
def compute(x, y):
    return x * y

def test_func(compute):
    result = compute(1, 2)
    print(result, type(compute))

test_func(compute)

#lambda匿名函数（只可临时使用一次）
def test_func(compute):
    result = compute(1, 2)
    print(result, type(compute))

test_func(lambda x, y: x + y)#lambda 传入参数： 函数体（一行）

