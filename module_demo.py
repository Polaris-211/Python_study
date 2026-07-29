#inport 模块名
#模块名.功能名()
import time
print("hello")
time.sleep(5) #通过. 使用模块内功能（类、函数、变量）
print("world")

#from 模块名 import 功能名  针对某一个功能使用
#功能名()
from time import sleep
sleep(5)

from time import *  #*导入全部功能
sleep(5)

#as别名
import time as t
t.sleep(5)

from time import sleep as sl
sl(5)

from my_mod import testB
testB(1, 2)