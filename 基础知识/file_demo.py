"""
文件操作
打开文件open(name, mode, encoding)
mode:r只读;w写入;a追加
encoding顺序并不是第三位，因此只能关键字传参
"""
# import time
#
# #打开文件
# f = open("D:/test/tree.txt", "r", encoding="UTF-8")
# print(type(f))
#
# #read()文件读取（每次读取会续接上一次读取的位置）
# #文件对象.read(num)  nun单位字节（换行算一个字节），未传入则表示读取所有文件
# print(f.read(10))
#
# #readlines()  整个文件内容一次性读取，返回列表，每一行数据为一个元素
# lines = f.readlines()
# print(type(lines))
# print(lines)
#
# #readline()  一次读取一行
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# print(line1)
# print(line2)
# print(line3)
#
# #for循环读取行
# for line in f:
#     print(line)
#
# #close()文件关闭
# f.close()
# time.sleep(500000)#暂停运行500000秒
#
# #with open 自动close
# with open("D:/test/tree.txt", "r", encoding="UTF-8") as f:
#     for line in f:
#         print(line)
# time.sleep(500000)

#f.write()文件写入（写入内存缓冲区）
# f = open("D:/test/test.txt", "w", encoding="UTF-8") #文件不存在则创建
# f.write("Hello World!")
# #f.flush()内容刷新（一次性写入硬盘）
# # f.flush()
# f.close() #内置flush功能

# f = open("D:/test/test.txt", "w", encoding="UTF-8")#文件存在则覆盖
# f.write("黑马程序员")
with open("test.txt", "w+") as f:
    ls = ["AAA", "BBB", "CCC"]
    f.writelines(ls)
    f.seek(0)
    for line in f:
        print(line)

#f.seek(offset(偏移字节数),whence=0(0:文件头部  1:当前位置  2:文件尾部))

#文件追加a
# f = open("D:/test/test.txt", "a", encoding="UTF-8")
# f.write("\n学Python最佳选择")
# f.close()