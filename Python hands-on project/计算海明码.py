def calc_parity_bits_length(m):
    """计算需要多少个校验位 r"""
    r = 0
    while (2 ** r) < (m + r + 1):
        r += 1
    return r

def insert_parity_bits(data):
    """把数据位插入到海明码中，空出校验位位置"""
    m = len(data)
    r = calc_parity_bits_length(m)
    n = m + r
    hamming = ['0'] * n
    j = 0  # 数据位指针
    for i in range(1, n+1):
        if (i & (i-1)) == 0:  # 校验位位置（2的幂）
            hamming[i-1] = '0'  # 先占位
        else:
            hamming[i-1] = data[j]
            j += 1
    return hamming, r

def set_parity_bits(hamming, r):
    """计算校验位值"""
    n = len(hamming)
    for i in range(r):
        parity_pos = 2 ** i
        parity = 0
        for j in range(1, n+1):
            if j & parity_pos and j != parity_pos:
                parity ^= int(hamming[j-1])
        hamming[parity_pos-1] = str(parity)
    return hamming

def hamming_encode(data):
    """完整编码过程"""
    hamming, r = insert_parity_bits(data)
    hamming = set_parity_bits(hamming, r)
    return ''.join(hamming)

def detect_error(hamming):
    """检测并返回错误位置（1-base），0表示无错"""
    n = len(hamming)
    r = calc_parity_bits_length(n - calc_parity_bits_length(n))
    error_pos = 0
    for i in range(r):
        parity_pos = 2 ** i
        parity = 0
        for j in range(1, n+1):
            if j & parity_pos:
                parity ^= int(hamming[j-1])
        if parity != 0:
            error_pos += parity_pos
    return error_pos

def correct_error(hamming):
    """检测并纠正单比特错误"""
    error_pos = detect_error(hamming)
    if error_pos == 0:
        return hamming, 0
    else:
        idx = error_pos - 1
        hamming[idx] = '1' if hamming[idx] == '0' else '0'
        return hamming, error_pos

# ===================== 使用示例 =====================
data = "1011"  # 4位数据
encoded = hamming_encode(data)
print("原数据:", data)
print("编码海明码:", encoded)

# 模拟传输出错（第5位翻转）
received = list(encoded)
received[4] = '1' if received[4] == '0' else '0'
print("接收码（含错误）:", ''.join(received))

# 检测并纠正
corrected, error_pos = correct_error(received)
print("纠正后的码:", ''.join(corrected))
print("错误位置:", error_pos)
