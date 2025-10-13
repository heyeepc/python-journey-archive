class IPAddress:
    def __init__(self, ip_str):
        # 1. 初始化属性：存储IP地址字符串
        self.address = ip_str
        
        # 2. 计算属性/状态：判断是否为私有地址
        self.is_private = self._check_is_private(ip_str)

    def _check_is_private(self, ip_str):
        """这是一个辅助方法（通常以下划线开头），用于内部判断私有地址。"""
        
        # 将IP地址拆分成四段，方便进行数字或前缀检查
        parts = ip_str.split('.')
        
        if not parts or len(parts) != 4:
            # 简单的无效地址处理（忽略复杂校验，只检查格式）
            return False 

        # 转换为整数方便范围判断
        try:
            p1 = int(parts[0])
            p2 = int(parts[1])
        except ValueError:
            # 如果转换失败（比如地址里有字母），也视为非私有
            return False

        # 规则 1: 10.0.0.0/8
        if p1 == 10:
            return True
        
        # 规则 2: 172.16.0.0/12 (即 172.16 到 172.31)
        # 注意这里需要判断第一段和第二段
        if p1 == 172 and 16 <= p2 <= 31:
            return True

        # 规则 3: 192.168.0.0/16
        if p1 == 192 and p2 == 168:
            return True
        
        # 不符合任何私有地址规则，则返回 False
        return False


    def display_info(self):
        """
        方法实现：打印出该IP地址的详细信息。
        需要访问并使用我们在__init__中设置的两个属性：self.address 和 self.is_private。
        """
        # 使用 f-string (格式化字符串) 打印信息
        print(f"IP地址: {self.address}", end=", ")
        print(f"是否为私有地址: {self.is_private}")

# ----------------------------------------------------
# 示例用法和测试
print("--- 运行测试 ---")

addr1 = IPAddress("192.168.10.5")
addr1.display_info()

addr2 = IPAddress("8.8.8.8")
addr2.display_info()

addr3 = IPAddress("172.17.20.1")
addr3.display_info()

addr4 = IPAddress("10.5.5.5")
addr4.display_info()

addr5 = IPAddress("172.32.0.1") # 不在 16-31 范围内，应为 False
addr5.display_info()
