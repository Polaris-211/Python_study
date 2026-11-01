# 注解
import random
import json

var_1: int = 10
var_2: str = "hello"
var_3: bool = True


# 类对象类型注解
class Student:
    pass


stu: Student = Student()
# 容器类型注解
my_list: list = [1, 2, 3]
my_tuple: tuple = (1, 2, 3)
my_dict: dict = {"a": 1, "b": 2, "c": 3}
# 容器类型详细注解
my_list: list[int] = [1, 2, 3]
my_tuple: tuple[int, str, bool] = (1, "hello", True)
my_dict: dict[str, int] = {"a": 1, "b": 2, "c": 3}


def func():
    return 10


# TYPE:类型 在注释中注解
var_1 = random.randint(1, 10)  # type: int
var_2 = json.loads('{"name":"zhangsan"}')  # type:dict[str, str]
var_3 = func()  # type:int


# 函数和方法的类型注解
#对形参类型注解
def add(x: int, y: int):
    return x + y

#对返回值类型注解
def func(data: list) -> list:
    return data

print(func(1))

#Union类型 定义联合类型注解
from typing import Union
my_list: list[Union[str, int]] = [1, 2, "itheima", "itcast"]
my_dict: dict[str, Union[str, int]] = {"name": "周杰轮", "age": 10}

def func(data: Union[int, str]) -> Union[int, str]:
    pass
func()