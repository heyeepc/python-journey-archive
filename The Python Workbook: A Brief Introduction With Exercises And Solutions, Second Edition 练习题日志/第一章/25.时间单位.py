#本练习将逆转练习24的过程。开发一个程序，首先读取用户输入的秒数。然后，程序应该以D:HH:MM:SS的形式显示等量的时间，其中D、HH、MM 和SS分别代表天数、小时、分钟和秒。小时、分钟和秒都应该格式化，使它们刚好显示为两位数字。
#使用研究技能确定，需要在格式说明符中包含哪些额外字符，以便在数字格式化为特定宽度时，使用前导零而不是前导空格。
SECONDS_PER_DAY = 24 * 60 * 60  # 86400 秒
SECONDS_PER_HOUR = 60 * 60      # 3600 秒
SECONDS_PER_MINUTE = 60         # 60 秒

total_seconds_str = input("请输入总秒数（非负整数）：")
total_seconds = int(total_seconds_str)
   #计算天数
days = total_seconds // SECONDS_PER_DAY
remaining_seconds = total_seconds % SECONDS_PER_DAY

  # 计算小时数
hours = remaining_seconds // SECONDS_PER_HOUR
remaining_seconds = remaining_seconds % SECONDS_PER_HOUR

 # 计算分钟数
minutes = remaining_seconds // SECONDS_PER_MINUTE
remaining_seconds = remaining_seconds % SECONDS_PER_MINUTE

  # 最终秒数
seconds = remaining_seconds

formatted_time = f"{days}:{hours:02d}:{minutes:02d}:{seconds:02d}"

print(f"\n等量的时间是：{formatted_time}")
