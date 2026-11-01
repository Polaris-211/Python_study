def print_file_info(file_name):
    """
    功能：将文件读取到控制台
    :param file_name:文件路径
    :return:None
    """
    f = None
    try:
        f = open(file_name, 'r', encoding='utf-8')
        print(f.read())
    except Exception as e:
        print("文件出现异常")
    finally:
        if f:
            f.close()


def append_to_file(file_name,data):
    """
    功能：将指定内容加到指定文件
    :param file_name: 文件路径
    :param data: 追加数据
    :return: None
    """
    f = open(file_name, 'a', encoding='utf-8')
    f.write(data)
    f.write("\n")
    f.close()

if __name__ == '__main__':
    print_file_info("D:/test/tree.txt")
    append_to_file("D:/test/tree.txt","传智教育")