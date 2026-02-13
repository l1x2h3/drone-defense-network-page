import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

# 设置中文字体（兼容多平台）
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 数据准备
pages = ['YOLO检测页', '入侵统计页', '信号处理页', '关于页', '主页', '其它']
percentages = [48.68, 38.39, 4.31, 3.86, 2.89, 1.87]

# 创建画布（增加右侧空间容纳图例）
fig, ax = plt.subplots(figsize=(11, 7), dpi=100)

# 生成科技蓝渐变色（从深到浅）
colors_gradient = plt.cm.Blues(np.linspace(0.9, 0.3, len(pages)))

# 绘制饼图（90度起始使最大扇区位于12点钟方向）
wedges, texts = ax.pie(
    percentages,
    startangle=90,
    colors=colors_gradient,
    wedgeprops={'edgecolor': 'white', 'linewidth': 2.5},
    textprops={'fontsize': 14}  # 预留标签空间（实际隐藏）
)

# 隐藏默认标签（仅用图例展示）
for text in texts:
    text.set_visible(False)

# 添加中心圆环营造环形图效果
centre_circle = plt.Circle((0, 0), 0.65, fc='white')
ax.add_artist(centre_circle)

# 设置标题（居中+适当上移避免与图例重叠）
ax.set_title('各页面加载时间占总用时比例', 
             fontsize=22, 
             fontweight='bold',
             pad=25)  # 标题与图表间距

# 生成图例（优化排版与可读性）
colors = [w.get_facecolor() for w in wedges]
handles = [
    mpatches.Patch(
        color=colors[i], 
        label=f"{pages[i]}: {percentages[i]:.2f}%"
    ) for i in range(len(pages))
]

# 图例定位在饼图右侧（避免溢出画布）
ax.legend(
    handles=handles,
    loc='upper left',
    bbox_to_anchor=(1.02, 1.0),  # 精确控制图例位置
    fontsize=14,
    frameon=False,
    labelspacing=0.7,   # 减小图例项间距
    handlelength=1.8,   # 缩短色块长度
    handleheight=1.2    # 降低色块高度
)

# 确保饼图为正圆形
ax.axis('equal')

# 自动调整布局防止元素重叠
plt.tight_layout(rect=[0, 0, 0.85, 1])  # 为右侧图例预留15%空间

# 保存高清图片（可选）
# plt.savefig('page_loading_distribution.png', dpi=300, bbox_inches='tight')

plt.show()