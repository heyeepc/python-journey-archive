import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib

# 中文显示
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

# 功能区分类函数
def classify_area(name):
    if any(keyword in name for keyword in ['宿舍', '舍', '热泵']):
        return '宿舍'
    elif any(keyword in name for keyword in ['食堂']):
        return '食堂'
    elif any(keyword in name for keyword in ['楼', '教学', '实验', '种子']):
        return '教学楼'
    elif any(keyword in name for keyword in ['办公室', '办公', '中心', '司法']):
        return '办公楼'
    elif any(keyword in name for keyword in ['体育', '体育馆']):
        return '体育设施'
    else:
        return '其他'

# 读取数据
df = pd.read_excel('data.xlsx', engine='openpyxl')
df['采集时间'] = pd.to_datetime(df['采集时间'])
df['区域类型'] = df['水表名'].apply(classify_area)
df['日期'] = df['采集时间'].dt.date
daily_usage = df.groupby(['区域类型', '日期'])['用量'].sum().reset_index()

# 画图
plt.figure(figsize=(12, 6))
sns.lineplot(data=daily_usage, x='日期', y='用量', hue='区域类型')
plt.title("校园不同功能区每日用水趋势")
plt.xlabel("日期")
plt.ylabel("总用水量")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
