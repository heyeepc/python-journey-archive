#地球表面是弯曲的，经度之间的距离随纬度而变化。因此，求地球表面两点之间的距离比简单地使用勾股定理要复杂得多。设（t1，g1）和（t2，g2）为地球表面两点的经纬度。这两点在地球表面的距离为（单位是千米）：
#距离==6371.01*arccos(sin(t)*sin(t2)+cos(t)*cos(t2)*cos(g1-g2))
#上述方程中的值 6371.01不是随机选取的。它是地球的平均半径，以千米为单位。
#创建一个程序，允许用户输入地球上两点的经度和纬度（以度为单位）。程序应该显示这两点在地球表面的距离，以千米为单位。
#Python的糟糕的缩进
import math

def great_circle_distance(lat1, lon1, lat2, lon2):
    """
    计算大圆距离（单位：千米）
    参数:
        lat1, lon1: 第一点的纬度和经度（弧度）
        lat2, lon2: 第二点的纬度和经度（弧度）
    返回:
        两点之间的表面距离（千米）
    """
    # 地球平均半径（千米）
    R = 6371.01
    return R * math.acos(
        math.sin(lat1) * math.sin(lat2) +
        math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2)
    )

def deg_to_rad(deg):
    """度转换为弧度"""
    return deg * math.pi / 180.0

def main():
    print("请输入第一个点的纬度和经度（单位：度）：")
    lat1_deg = float(input("  纬度 t1: "))
    lon1_deg = float(input("  经度 g1: "))
    
    print("\n请输入第二个点的纬度和经度（单位：度）：")
    lat2_deg = float(input("  纬度 t2: "))
    lon2_deg = float(input("  经度 g2: "))
    
    # 转换为弧度
    lat1 = deg_to_rad(lat1_deg)
    lon1 = deg_to_rad(lon1_deg)
    lat2 = deg_to_rad(lat2_deg)
    lon2 = deg_to_rad(lon2_deg)
    
    # 计算距离
    distance = great_circle_distance(lat1, lon1, lat2, lon2)
    
    print(f"\n两点之间的球面距离为：{distance:.2f} 千米")

if __name__ == "__main__":
    main()
