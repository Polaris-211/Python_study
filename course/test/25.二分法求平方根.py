"""
描述
设计一个用二分法计算一个大于或等于 1 的实数 n 的平方根的函数sqrt_binary(n)，
计算精度控制在计算结果的平方与输入的误差不大于1e-6。


注：初始区间取[0,n]


输入格式
输入一个实数 n（大于或等于1）


输出格式
第一行输出用自己设计的函数计算得到的平方根


第二行输出用math库开平方函数计算得到的平方根
"""
import math
def sqrt_binary(n):
    left = 0
    right = n
    while True:
        mid = (left + right) / 2
        if abs(mid ** 2 - n) <= 1e-6:
            return mid
        if mid ** 2 > n:
            right = mid
        else:
            left = mid

if __name__ == '__main__':
    n = float(input())
    print(sqrt_binary(n))
    print(math.sqrt(n))