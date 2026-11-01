"""
输入一个小于等于12的整数n，逐个输出字符串 '人生苦短我用python' 中前n个字符，每个字符后输出一个半角逗号和一个空隔。

输入
一个小于等于12的整数n
输出
'人生苦短我用python' 中前n个字符
"""


print(map(lambda x: x + ',', "人生苦短我用python"[:int(input()):]))
print(*list("人生苦短我用python"[:int(input())]), sep=", ", end=", ")
[print(c, end=", ") for c in "人生苦短我用python"[:int(input())]]