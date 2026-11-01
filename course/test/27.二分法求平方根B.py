import math
def sqrt_binary(n, a):
    left = 0
    right = n + 0.25
    while True:
        mid = (left + right) / 2
        if abs(mid ** 2 - n) <= a:
            return mid
        if mid ** 2 > n:
            right = mid
        else:
            left = mid

if __name__ == '__main__':
    n, a = map(float, input().split(','))
    print(f"{sqrt_binary(n, a):.8f}")
    print(f"{math.sqrt(n):.8f}")