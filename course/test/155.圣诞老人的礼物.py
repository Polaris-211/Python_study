"""
描述
圣诞节来临了，在城市A中，圣诞老人准备分发糖果，现在有很多箱不同的糖果，每箱糖果都有自己的价值和重量，
每箱糖果都可以拆分成任意散装组合带走。圣诞老人的驯鹿最多只能承受一定重量的糖果，请问圣诞老人最多能带走多大价值的糖果。


输入
输入的第一行由两个部分组成，分别为糖果箱数正整数n（1<=n<=100）,驯鹿能承受的最大重量正整数m(0<m<10000)，现个数用空格分隔


其余n行每行对应一箱糖果，由两部分整数v和w组成，分别为一箱糖果的价值和重量，中间用空格分隔


输出
圣诞老人能带走的糖果的最大总价值，保留1位小数
"""


class Gift:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.unit_value = value / weight


n, m = map(int, input().split())

gifts = []
for _ in range(n):
    v, w = map(int, input().split())
    gifts.append(Gift(v, w))

gifts.sort(key=lambda g: g.unit_value, reverse=True)

total_value = 0.0
capacity = m

for g in gifts:
    if capacity >= g.weight:
        total_value += g.value
        capacity -= g.weight
    else:
        total_value += g.unit_value * capacity
        break

print(f"{total_value:.1f}")