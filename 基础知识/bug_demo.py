#捕获异常
# try :
#     f = open("D:/test/abc.txt", "r", encoding="UTF-8")
# except :
#     print("error")
#     f = open("D:/test/abc.txt", "w", encoding="UTF-8")

#捕获指定异常
# try:
#     print(name)
#     # 1/0
# except NameError as e:
#     print("出现变量未定义的异常")
#     print(e)
#
# #捕获多个异常
# try:
#     # print(name)
#     1/0
# except (NameError, ZeroDivisionError) as e:
#     print("出现异常")

#捕获所有异常Exception
try: #有可能有异常
    f = open("D:/test/123.txt", "r", encoding="UTF-8")
except Exception as e: #有异常执行
    f = open("D:/test/123.txt", "w", encoding="UTF-8")
else: #无异常执行（可选）
    print("haogaoxin")
finally: #都执行（可选）
    print("有没有异常都执行")
    f.close()

#异常的传递
def func1():
    print("func1 开始执行")
    num = 1/0
    print("func1 结束执行")

def func2():
    print("func2 开始执行")
    func1()
    print("func2 结束执行")

def main():
    try:
        func2()
    except Exception as e:
        print(f"出现异常了{e}")

main()