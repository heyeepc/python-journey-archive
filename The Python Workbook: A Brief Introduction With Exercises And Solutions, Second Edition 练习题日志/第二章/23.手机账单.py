#一个特别的手机套餐包括50分钟的通话时间和50条短信，每月15美元。每增加一分钟的通话时间，费用为0.25美元；每增加一条短信，费用为0.15美元。
#所有手机话费都包括额外的$0.44费用，用于支持911呼叫中心，整个账单（包括 911费用）需要缴纳5%的销售税。
#编写一个程序，读取用户在一个月内使用的分钟数和文本消息。显示基本收费、额外分钟收费（如有）、额外的短信费用（如有）、
#911费用、税金和账单总额。如果用户在这些类别中产生了费用，则只显示额外的分钟和文本消息费用。确保所有费用都用两位小数

# 手机套餐账单计算程序
import sys

try:
    call_minutes = float(input("输入通话时间(分): ").strip())
    text_messages = int(input("输入短信数量: ").strip())
except ValueError:
    print("输入无效：请确保通话时间为数字，短信数量为整数。")
    sys.exit(1)

if call_minutes < 0 or text_messages < 0:
    print("输入无效：通话时间和短信数量不能为负。")
    sys.exit(1)

PACKAGE_FEE = 15.00
INCL_MINUTES = 50
INCL_TEXTS = 50
EXTRA_MIN_RATE = 0.25
EXTRA_TEXT_RATE = 0.15
FEE_911 = 0.44
TAX_RATE = 0.05

# 计算额外费用
extra_minutes = max(0.0, call_minutes - INCL_MINUTES)
extra_min_charge = extra_minutes * EXTRA_MIN_RATE

extra_texts = max(0, text_messages - INCL_TEXTS)
extra_text_charge = extra_texts * EXTRA_TEXT_RATE

# 小计（包含套餐费、额外费和 911 费），然后计算税和总额
subtotal = PACKAGE_FEE + extra_min_charge + extra_text_charge + FEE_911
tax = subtotal * TAX_RATE
total = subtotal + tax

# 输出（只在有额外费用时显示对应行），金额保留两位小数
print("\n--- 本月账单 ---")
print(f"基本收费 (套餐) : ${PACKAGE_FEE:.2f}")
if extra_min_charge > 0:
    print(f"额外通话费 ({extra_minutes:.0f} 分) : ${extra_min_charge:.2f}")
if extra_text_charge > 0:
    print(f"额外短信费 ({extra_texts} 条) : ${extra_text_charge:.2f}")
print(f"911 支援费        : ${FEE_911:.2f}")
print(f"税金 (5%)         : ${tax:.2f}")
print(f"账单总额          : ${total:.2f}")
