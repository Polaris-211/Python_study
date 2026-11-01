# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 22:35:27 2026

描述
 给定一个以秒为单位的时间t，要求用“HH:MM:SS”的格式来表示这个时间。
 HH表示时间，MM 表示分钟， SS 表示秒，都是整数，不足2位时前面补“0”。
 例如，若 t = 1，则应输出是“00:00:01”；若 t = 3661，则输出“1:1:1”。
 

输入
输入只有一行，为一个整数（0 <= t <= 86399）。


输出
输出只有一行，是以“HH:MM:SS”的格式所表示的时间，不包括引号。

@author: Polaris
"""

time = int(input())
second = time%60
minute0 = time//60
hour = minute0//60
minute1 = minute0%60
print(f"{hour:02d}:{minute1:02d}:{second:02d}")

