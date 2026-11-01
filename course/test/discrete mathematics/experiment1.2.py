r"""
1.2构造合式公式的真值表
问题描述：给出任意命题变元（不超过3个变元，如：P,Q,R）的合式公式。
输入说明：需要用特定的字符串将联结词表示（如~可以表示非，->表示蕴涵，
<->表示等价，\/表示析取，/\表示合取，中间不加任何空格），输入合式公式。
输出说明：构造真值表有如下约定：
①  命题变元按字典序排列；
②  对公式的每个解释，以二进制数从小到大或者从大到小顺序列出；
③  只输出变元和公式的真值。
输入样例：~P\/Q/\R
输出样例：
P	Q	R	(~P\/Q)/\R
0	0	0	0
0	0	1	1
0	1	0	0
0	1	1	1
1	0	0	0
1	0	1	0
1	1	0	0
1	1	1	1
输入方式：控制台
"""
import pandas as pd

CONNECTIVES = (('<->', 1, True), ('->', 2, False), ('\\/', 3, True), ('/\\', 3, True))

def unwrap(formula):
    if not formula.startswith('('):
        return formula
    depth = 0
    for i, ch in enumerate(formula):
        depth += (ch == '(') - (ch == ')')
        if depth == 0:
            return formula[1:-1] if i == len(formula) - 1 else formula
    return formula

def main_connective(formula):
    depth = 0
    found = None
    i = 0
    while i < len(formula):
        if formula[i] == '(':
            depth += 1
        elif formula[i] == ')':
            depth -= 1
        elif depth == 0:
            for op, rank, left_assoc in CONNECTIVES:
                if not formula.startswith(op, i):
                    continue
                if found is None or rank < found[2] or (rank == found[2] and left_assoc):
                    found = (i, op, rank)
                i += len(op) - 1
                break
        i += 1
    return None if found is None else (found[0], found[1])

def value(formula, env):
    formula = unwrap(formula)
    split = main_connective(formula)
    if split is None:
        if formula.startswith('~'):
            return 1 - value(formula[1:], env)
        return env[formula]
    index, op = split
    left = value(formula[:index], env)
    right = value(formula[index + len(op):], env)
    if op == '/\\':
        return left & right
    if op == '\\/':
        return left | right
    if op == '->':
        return int(left <= right)
    return int(left == right)

formula = input()
names = sorted({ch for ch in formula if ch.isalpha()})
rows = []
for i in range(1 << len(names)):
    env = {name: (i >> (len(names) - 1 - j)) & 1 for j, name in enumerate(names)}
    row = dict(env)
    row[formula] = value(formula, env)
    rows.append(row)
print(pd.DataFrame(rows).to_string(index=False))
