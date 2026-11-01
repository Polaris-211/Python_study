from pyecharts.charts import Bar, Timeline
from pyecharts.globals import ThemeType
from pyecharts.options import *

bar1 = Bar()
bar1.add_xaxis(["中国", "美国", "英国"])
bar1.add_yaxis("GDP", [30, 20, 10], label_opts=LabelOpts(position="right"))
bar1.reversal_axis()

bar2 = Bar()
bar2.add_xaxis(["中国", "美国", "英国"])
bar2.add_yaxis("GDP", [50, 30, 20], label_opts=LabelOpts(position="right"))
bar2.reversal_axis()

bar3 = Bar()
bar3.add_xaxis(["中国", "美国", "英国"])
bar3.add_yaxis("GDP", [70, 40, 30], label_opts=LabelOpts(position="right"))
bar3.reversal_axis()

timeline = Timeline({"theme":ThemeType.LIGHT})
timeline.add(bar1, "2021GDP")
timeline.add(bar2, "2022GDP")
timeline.add(bar3, "2023GDP")


timeline.add_schema(
    play_interval=1000, #自动播放时间间隔，单位毫秒
    is_timeline_show=True, #是否显示时间线
    is_auto_play=True, #是否自动播放
    is_loop_play=True #是否循环播放
)

timeline.render()

