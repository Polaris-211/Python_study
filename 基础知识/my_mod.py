__all__ = ['testA'] #inmort* 时，只能用all变量里面的函数


def testA(a, b):
    print(a + b)
if __name__ == '__main__': #引用函数导入时不执行
    testA(1, 2)

def testB(a, b):
    print(a * b)

def testB(a, b): #不同模块同名功能，后导入的覆盖先导入的
    print(a / b)

