import numpy as np
import pandas as pd

# 创建身高数据 (米)
heights = np.linspace(1.50, 1.90, 50) # 从1.50米到1.90米，生成50个身高数据

# 创建体重数据 (公斤)
weights = np.linspace(40, 100, 50) # 从40公斤到100公斤，生成50个体重数据

# 创建一个网格，表示所有身高-体重的组合
height_mesh, weight_mesh = np.meshgrid(heights, weights)

# 计算每个组合的 BMI
bmi_mesh = weight_mesh / (height_mesh ** 2)

# 根据 BMI 分类体重状态
def get_weight_status(bmi):
    if bmi < 18.5:
        return '过轻'
    elif 18.5 <= bmi < 24:
        return '正常'
    elif 24 <= bmi < 28:
        return '超重'
    else:
        return '肥胖'

# 将 BMI 转换为体重状态
weight_status_mesh = np.vectorize(get_weight_status)(bmi_mesh)

# 为了绘图方便，我们将数据整理成 Pandas DataFrame
data = pd.DataFrame({
    '身高(m)': height_mesh.flatten(),
    '体重(kg)': weight_mesh.flatten(),
    'BMI': bmi_mesh.flatten(),
    '体重状态': weight_status_mesh.flatten()
})

# 定义颜色映射
status_colors = {
    '过轻': 'skyblue',  # 浅蓝色
    '正常': 'lightgreen', # 浅绿色
    '超重': 'orange',    # 橙色
    '肥胖': 'red'       # 红色
}

import matplotlib.pyplot as plt

# 确保能显示中文
plt.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

plt.figure(figsize=(10, 8))

# 遍历不同的体重状态，分别绘制散点图，并赋予不同的颜色
for status, color in status_colors.items():
    subset = data[data['体重状态'] == status]
    plt.scatter(subset['身高(m)'], subset['体重(kg)'], color=color, label=status, alpha=0.7)

# 添加标题和标签
plt.title('身高-体重与BMI关系图')
plt.xlabel('身高 (米)')
plt.ylabel('体重 (公斤)')

# 添加图例
plt.legend(title='体重状态')

# 添加网格
plt.grid(True, linestyle='--', alpha=0.6)

# 显示图表
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

# 确保能显示中文
plt.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

plt.figure(figsize=(10, 8))

# 使用 Seaborn 的 scatterplot 函数
# x 轴是身高，y 轴是体重，hue 参数根据 '体重状态' 自动着色
# palette 参数使用我们之前定义的颜色映射
sns.scatterplot(x='身高(m)', y='体重(kg)', hue='体重状态', data=data,
                palette=status_colors, s=100, alpha=0.7) # s 参数控制点的大小

# 添加标题和标签
plt.title('身高-体重与BMI关系图')
plt.xlabel('身高 (米)')
plt.ylabel('体重 (公斤)')

# 添加网格
plt.grid(True, linestyle='--', alpha=0.6)

# 显示图表
plt.show()
