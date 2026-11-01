# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 23:51:54 2026

描述
 

一元二次方程ax2+bx+c=0，a、b、c的值由用户在三行中输入，
根据用户输入的数值求解方程的实数解：


如果a值 为0，根据b值判断方程是否有解并输出，如果a与b同时为0，则输出Data error!


如果方程无实数解，输出“该方程无实数解”；


如果方程有两个相同的实数解，输出一个解；


如果方程有两个不同的实数解，在一行内按从大到小顺序输出方程的两个解，用空格分隔


输入格式 
 输入三行数据, 每行输入一个实数
 

输出格式
方程的解

@author: Polaris
"""
def solution (a, b, c):
    if (b**2)-(4*a*c) < 0 :
        print("该方程无实数解")
    elif (b**2)-(4*a*c) == 0:
        print((-b)/(2*a))
    elif (b**2)-(4*a*c) > 0 :
        x1 =((-b)+((b**2)-(4*a*c))**0.5)/(2*a)
        x2 =((-b)-((b**2)-(4*a*c))**0.5)/(2*a)
        if x1 > x2:
            print(x1, x2)
        else:
            print(x2, x1)

    
    
import sys                              # 导入 sys 模块，用于读取标准输入
data = sys.stdin.read().split()         # 一次性读取全部输入，按空白字符切分成列表
a, b, c = map(float, data[:3])          # 取前三个元素转成浮点数，依次赋值给 a, b, c
if a == 0 :
    if b == 0:
        print ("Data error!")
    else:
        print (-c/b)
else :
    solution(a, b, c)
