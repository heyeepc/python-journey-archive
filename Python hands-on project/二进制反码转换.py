def get_ones_complement_v2(binary_string):
    if not all(bit in '01' for bit in binary_string):
        print("错误：输入包含非二进制字符！")
        return None
    complement_list = ['1' if bit == '0' else '0' for bit in binary_string]
    return "".join(complement_list)

binary_num = input("输入数字")
complement_num = get_ones_complement_v2(binary_num)
if complement_num is not None:
    print(f"原二进制串: {binary_num}")
    print(f"反码: {complement_num}")
