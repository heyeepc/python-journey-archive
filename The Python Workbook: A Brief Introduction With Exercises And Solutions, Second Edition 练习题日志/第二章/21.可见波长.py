#编写一个程序，读取用户输入的波长并报告其颜色。如果用户输入的波长在可见光谱之外，则显示适当的错误消息。
# 定义可见光谱范围和对应的颜色，使用列表嵌套元组
VISIBLE_WAVELENGTHS = [
    ((380, 450), "紫色"),
    ((450, 495), "蓝色"),
    ((495, 570), "绿色"),
    ((570, 590), "黄色"),
    ((590, 620), "橙色"),
    ((620, 750), "红色"),
]

def find_wavelength_color():
    """读取用户输入的波长并报告其颜色。"""
    
    # 1. 获取用户输入
    while True:
        try:
            # 尝试将用户输入转换为浮点数
            wavelength_input = input("请输入波长 (单位: 纳米): ")
            wavelength = float(wavelength_input)
            break # 成功转换为浮点数则退出循环
        except ValueError:
            # 捕获用户输入非数字的情况
            print("错误: 输入无效。请输入一个数字作为波长。")
            continue

    # 2. 核心判断逻辑
    
    # 初始化一个标志，用于判断是否找到了颜色
    color_found = False
    
    # 遍历我们定义的可见光谱列表
    for (min_wl, max_wl), color_name in VISIBLE_WAVELENGTHS:
        # (min_wl, max_wl) 是元组中的范围，color_name 是颜色名称
        
        # 判断：如果输入的波长大于等于范围的最小值 并且 小于范围的最大值
        # 注意：这里我们使用 >= 和 <，这是处理连续范围的标准做法，
        # 例如 450nm 被认为是“蓝色”范围的起点。
        if min_wl <= wavelength < max_wl:
            print(f"波长 {wavelength} nm 对应的颜色是: {color_name}")
            color_found = True
            break # 找到颜色后，立即退出循环，提高效率

    # 3. 处理可见光谱之外的情况
    
    if not color_found:
        # 如果循环结束，color_found 仍然为 False，说明波长不在任何定义的范围内
        
        # 我们可以进一步判断它是在可见光范围之外的哪一侧 (小于380或大于750)
        # 找出可见光范围的绝对最小值和最大值
        MIN_VISIBLE = 380
        MAX_VISIBLE = 750
        
        if wavelength < MIN_VISIBLE:
            print(f"错误: {wavelength} nm 超出了可见光谱范围。它属于 **紫外线 (UV)** 或更短的电磁波。")
        elif wavelength >= MAX_VISIBLE:
            print(f"错误: {wavelength} nm 超出了可见光谱范围。它属于 **红外线 (IR)** 或更长的电磁波。")
        else:
            # 理论上不会发生，除非范围有空隙 (例如 450-450.1nm 这种极小的空隙)
            print("错误: 波长在可见光范围内但未匹配到具体颜色。请检查定义的范围。")

# 运行函数
find_wavelength_color()
