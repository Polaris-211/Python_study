def str_reverse(s):
    """
    功能：反转字符串
    :param s: 被反转字符串
    :return: 反转后的字符串
    """
    return s[::-1]

def substr(s, x, y):
    """
    将字符串按x， y分割
    :param s: 原字符串
    :param x: 开始下标
    :param y: 结束下标
    :return: 切割下来的字字符串
    """
    return s[x:y]

if __name__ == '__main__':
    print(str_reverse("黑马程序员"))
    print(substr("黑马程序员", 1,3 ))