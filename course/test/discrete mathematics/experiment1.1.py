"""
1.1求命题逻辑运算的结果
问题描述：给出两个命题变元(例如：P=0，Q=1)的否定式、合取式、析取式、蕴含式、等价式的真值。
输入样例：0  1
输出样例：
P	Q	~P  ~Q  P/\Q  P\/Q  P->Q  P<->Q
0	1	 1	 0     0     1      1      0
输入方式：控制台
"""
import pandas as pd

def logic_operation(p, q):
    return pd.DataFrame({
        'P': [p],
        'Q': [q],
        '~P': [int(not p)],
        '~Q': [int(not q)],
        'P/\\Q': [p & q],
        'P\\/Q': [p | q],
        'P->Q': [int(p <= q)],
        'P<->Q': [int(p == q)]
    })

p, q = map(int, input().split())
print(logic_operation(p, q).to_string(index=False))