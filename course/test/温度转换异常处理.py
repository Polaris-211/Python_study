"""
温度的刻画有两个不同体系：摄氏度（Celsius）和华氏度（Fabrenheit）。

请编写程序将用户输入华氏度转换为摄氏度，或将输入的摄氏度转换为华氏度。

转换算法如下：（C表示摄氏度、F表示华氏度）
         C = ( F - 32 ) / 1.8
         F = C * 1.8 + 32
要求如下：
(1) 输入输出的摄氏度采用大写字母 C 或小写字母 c 结尾，温度可以是整数或小数，如：12.34C 指摄氏度 12.34 度；
(2) 输入输出的华氏度采用大写字母 F 或小字字母 f 结尾，温度可以是整数或小数，如：87.65F 指华氏度 87.65 度；
(3) 考虑异常输入的问题，如输入不合法则抛出异常；
(4) 使用input()获得测试用例输入时，不要增加提示字符串。

输入格式
输入一个带单位的温度

输出格式
输入正常，输出转换后的温度，保留小数点后2位小数。
当用户输入值末位不是“C、c、F、f”中的一个时，输出"输入错误，末位只能是'C','c','F','f'"
当检测到NameError错误时输出'试图访问的变量名不存在'
当检测到SyntaxError 错误时输出'存在语法错误'
"""
def temperature_conversion(temperature):
    try:
        if temperature[-1] in ['C', 'c']:
            return "{:.2f}F".format(eval(temperature[:-1]) * 1.8 + 32)
        elif temperature[-1] in ['F', 'f']:
            return "{:.2f}C".format((eval(temperature[:-1]) - 32) / 1.8)
        else:
            return "输入错误，末位只能是'C','c','F','f'"
    except NameError:
        return '试图访问的变量名不存在'
    except SyntaxError:
        return '存在语法错误'

print(temperature_conversion(input()))

