"""
回文素数是指一个数既是素数又是回文数。例如，131，既是素数又是回文数。
用户输入一个正整数 n , 请你在一行内输出从小到大排列的的前n个回文素数，
数字后面用一个空格进行分隔。
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
        if is_huiwen(i) and isPrime(i):
            print(i, end=' ')
            count += 1
        i += 1 if i == 2 else 2