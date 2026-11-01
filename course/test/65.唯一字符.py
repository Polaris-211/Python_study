"""
给定一个字符串，找到它的第一个不重复的字符，输出它的索引。如果不存在这种字符或空串，
则返回 -1。

本题字符串中只包含小写字母。
"""

def f(s):
    k={}
    if len(s)==0:
        return -1
    for i in s:
        if i in k:
            k[i]+=1
        else:
            k[i]=1
    p=sorted(k.items(),key=lambda x:x[1])
    if p[0][1]==1:
        return s.index(p[0][0])
    else:
        return -1
s=input()
print(f(s))
 