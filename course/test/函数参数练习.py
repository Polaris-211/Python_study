"""
描述
编写函数，可以接收任意多个整数并输出其中的最大值和所有整数之和。

扩展：接收任意多个整数，但是只输出用户指定个数的最大值及求和，如果用户不指定个数则输出所有的最大值和所有整数之和。


注意：

使用p=eval(input()) 格式接收键盘输入；

使用print输出函数调用返回结果

输入输出示例
输入： 1,2,3,4,5,6,7,8 输出： 8 36

输入 ：1,2,3,4,5,6,7,8,size=3 输出：3 6
"""
def max_and_sum(*args):
    return max(args), sum(args)

p = eval(input())
if isinstance(p, tuple):
    print(max_and_sum(*p))
else:
    print(max_and_sum(p))