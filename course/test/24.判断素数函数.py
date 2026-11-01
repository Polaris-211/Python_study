"""写一个函数isPrime(n)用于判断一个数字n是不是素数，用户输入一个正整数，
在一行内输出不大于该数的所有素数，各数后面用一个空格分隔。


输入格式
输入一个正整数


输出格式
不大于该数的所有素数，各数后面用一个空格分隔。
"""

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    n = int(input())
    for x in range(1, n + 1):
        if isPrime(x):
            print(x, end=' ')