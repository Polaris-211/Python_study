"""
描述
现有方程：f(x) = x3-5x2+10x-80=0, 已经f(x)在[0,10]区间单调递增，
f(0) = -80 < 0,  f(10) = 520>0, 用二分法求解方程在[0,10]之间的解。


输入
输入一个正整数n，当f(x) < 10-n 时认为f(x) = 0,即此时 x 为方程的给定区间的解。

输出
输出方程精确到小数点后第9位的解
"""

def f(x):
    return x**3 - 5 * x**2 + 10 * x - 80

n = int(input())
left, right = 0, 10

while True :
    mid = (left + right) / 2
    if abs(f(mid)) < 10**(-n):
        print(f"{mid:.9f}")
        break
    elif f(mid) < 0:
        left = mid
    else:
        right = mid