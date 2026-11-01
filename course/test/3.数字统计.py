# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 19:13:10 2026

让用户在一次输入时输入N个数字（ 2<= N<= 15 ，即每次输入的数字量不同），之间以“,”分隔。
然后组合显示：
(1)用户输入的数字个数；
(2)用户输入的最小数字；
(3)将用户输入的数字按从大到进行排列输出，数字之间以“,”作为分隔
(4)如果用户输入的数字小于26，则找到相对应的26个大写英文字母（1对应A,26对应Z）
并拼接在一起打印显示，如果输入的数字在1-26之外则不显示相应字母。
（例：程序输入214，则显示输出 “[bad] ”））。
输入 ：
第一行输入一个正整数n（1<=n<=4）
第二行输入N个数字，2<=N<=15
输出 ：
输入的数字个数
字个输入的最小数字
输入的数字从大到小排列
输入的数字所对应的字母


评判标准：


10分：输入数字1，可正确输出用户输入的数字个数
20分：输入数字2，在10分标准的基础上，正确输出用户输入的最小数字
40分：输入数字3，在20分的标准基础上，正确地将用户输入的数字按从大到小进行排序输出
50分：输入数字4，在40分的标准基础上，正确完成显示数字对应字母的环节

@author: Polaris
"""
num_list = []
def input_count(num_str):
    global num_list
    num_list = num_str.split(',')
    lenth = len(num_list)
    print (lenth)
    # print (num_list)
# def min_num():
#     min = 1e10
#     for str_n in num_list:
#         n = int (str_n)
#         if n < min :
#             min = n
#     print (min)
            
def sort_list():
    temp = sorted(num_list, key=int, reverse=True)
    print(",".join(temp))


def min_num():
    temp_list = sorted(num_list, key=int)
    print(int (temp_list[0]))

def match_letter():
    litter_list = []
    for num in num_list:
        n = int(num)
        if 1 <= n <= 26:
            litter = chr(64 + n)
            litter_list.append(litter)
        else :
            litter_list.append('')
    print(f'[{"".join(litter_list)}]')
        


    
    
n = int(input())
num_str = input()

input_count(num_str)

if n >= 2:
    min_num()
if n >= 3:
    sort_list()
if n >= 4:
    match_letter()

