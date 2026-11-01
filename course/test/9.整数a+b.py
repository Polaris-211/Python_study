# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 18:25:37 2026

描述
 

 每行输入两个整数a和b，计算并输出 a + b 的和。
 

输入
输入可能有多行，每行输入用空格分隔的两个整数，当直接输入回车时结束输入。


输出
每行输出对应输入的数据的和

@author: Polaris
"""
import sys                             
data = sys.stdin.read().split()   
n = 1
while n<= len(data):
    awn = int(data[n-1]) + int(data[n])
    n += 2
    print(awn)