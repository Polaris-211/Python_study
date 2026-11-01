from matplotlib import legend
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts

line1 = Line()
line1.add_xaxis(["中国", "美国", "英国"])
line1.add_yaxis("GDP",[100,30,1])

#全局配置项
line1.set_global_opts(
    title_opts = TitleOpts(title = "GDP展示", pos_left = "1%", pos_top = "1%"), #pos_left左右调整;center居中
    legend_opts = LegendOpts(is_show = True), #展示图例（默认显示）
    toolbox_opts = ToolboxOpts(is_show = True), #展示工具箱
    visualmap_opts = VisualMapOpts(is_show = True) #视觉映射
)

line1.render()