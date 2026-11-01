"""
描述
我的微信ID是大写字母WHUT后面的数字是两个素数连在一起，大的在前，小的在后，如果我告诉你两数的乘积是多少，
如果输入一个[0-9]之间的数字，你能统计出从1开始到我ID中的数字的序列里，一共出现多少次这个数字吗？

输入格式
第一行输入ID中两个素数的乘积
第二行输入一个[0-9]之间的数字

输出格式
第一行输出ID号
第二行输出数字的次数
"""

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def getID(n):
    for i in range(2, n):
        if n % i == 0 and isPrime(i) and isPrime(n // i):
            large, small = (n // i, i) if n // i > i else (i, n // i)
            return str(large) + str(small)

def countDigit(id, digit):
    count = 0
    d = str(digit)
    for i in range(1, int(id) + 1):
        count += str(i).count(d)
    return count

if __name__ == '__main__':
    n = int(input())
    digit = int(input())
    id = getID(n)
    print(f"WHUT{id}")
    print(countDigit(id, digit))

