"""描述
给定正整数a,b,c，求不定方程ax+by=c关于未知数x和y的所有非负整数解组数。


输入
输入为一行，包含三个正整数a、b、c，两个整数之间用单个空格隔开,
每个数均不大于1000.

输出
一个整数，即不定方程的非负整数解组数"""
a, b, c = map(int, input().split())
count = 0
for x in range(c // a + 1):
    for y in range((c - a * x) // b + 1):
        if a * x + b * y == c:
            count += 1
print(count)