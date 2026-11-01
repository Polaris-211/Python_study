"""
反素数(逆向拼写的素数)是指一个将其逆向拼写后也是一个素数的非回文数。
例如：13和31都是素数，且13和31都不是回文数，所以，13和31是反素数。
输入一个正整数 n , 请输出从小到大排列的的前n个反素数，
数字后面以一个空格进行分隔。
"""
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_huiwen(n):
    s = str(n)
    return s == s[::-1]

if __name__ == '__main__':
    n = int(input())
    count = 0
    i = 2
    while count < n:
        j = int(str(i)[::-1])
        if isPrime(i) and isPrime(j) and not is_huiwen(i):
            print(i, end=' ')
            count += 1
        i += 1 if i == 2 else 2