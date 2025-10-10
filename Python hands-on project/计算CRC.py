def crc_calculate(data_bits, generator_bits):
    """
    计算给定数据和生成多项式的 CRC 校验码（基于模2长除法）。

    :param data_bits: 待计算的数据位串 (例如 '1110')
    :param generator_bits: 生成多项式位串 (例如 '1011')
    :return: 3位的CRC校验码 (字符串形式)
    """
    # 1. 准备工作
    # G 的长度 (G的度数是 len(G) - 1)
    g_len = len(generator_bits)
    # CRC 的长度，即余数的位数，等于 G 的度数，所以是 g_len - 1 = 3
    crc_len = g_len - 1

    # 2. 扩展数据
    # 在数据后添加 (g_len - 1) 个 0
    # 待除数 D' = D + '000' (3个0)
    # dividend_list = ['1', '1', '1', '0', '0', '0', '0']
    dividend_list = list(data_bits + '0' * crc_len)

    # 将除数转换为列表方便操作
    # generator_list = ['1', '0', '1', '1']
    generator_list = list(generator_bits)

    # 3. 模 2 长除法
    # 只需要循环数据位串的长度次 (len(data_bits)=4)
    for i in range(len(data_bits)):
        # 如果当前首位是 '1'，则进行异或运算
        if dividend_list[i] == '1':
            # 将除数与当前窗口进行异或操作
            for j in range(g_len):
                # 模 2 减法（异或运算，XOR）
                # '1' XOR '0' = '1', '1' XOR '1' = '0'
                if dividend_list[i + j] == generator_list[j]:
                    dividend_list[i + j] = '0'
                else:
                    dividend_list[i + j] = '1'

    # 4. 提取校验码 (余数)
    # CRC校验码就是最后 crc_len 位的余数
    remainder = ""。join(dividend_list[-crc_len:])

    return remainder

# 待计算的数据 D (消息)
message = "1110"
# 除数 G (生成多项式 x^3 + x + 1)
generator = "1011"

# 计算 CRC
try:
    crc_result = crc_calculate(message, generator)

    print(f"待计算的数据 (D): {message}")
    print(f"生成多项式 C(X): {generator} (即 x^3 + x + 1)")
    print(f"CRC 校验码 (3位余数): {crc_result}")
    print("\n---")
    print(f"最终待发送的编码数据 (D + CRC): {message}{crc_result}")

except Exception as e:
    print(f"计算过程中发生错误: {e}")
