# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 23:03:35 2026

描述
 编写一个模拟运算的程序。在一行中依次输入两个整数（第二个整数不为0）
 和一个字符（仅考虑+、-、*、/、//、%），各输入间用空格分隔。
 输出用这两个整数和输入的字符构成的运算表达式并输出计算结果。 
 

输入
在一行中输入用空格分隔的两个整数和一个运算符（仅考虑+、-、*、/、//、%）


输出
表达式和运算结果（每个运算符号前后各有一个空格）

@author: Polaris
"""

str = input()
list = str.split(' ')
a = int(list[0])
b = int(list[1])
ob = list[2]
if ob == '+':
    print(f"{a} + {b} = {a+b}")
elif ob == '-':
    print(f"{a} - {b} = {a-b}")
elif ob == '*':
        print(f"{a} * {b} = {a*b}")
elif ob == '/':
    print(f"{a} / {b} = {a/b}")
elif ob == '//':
    print(f"{a} // {b} = {a//b}")
elif ob == '%':
    print(f"{a} % {b} = {a%b}")