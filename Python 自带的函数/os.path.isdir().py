import os
# 1. 判断一个存在的文件夹
folder_path = 'my_folder'
print(f"'{folder_path}' 是一个目录吗？ {os.path.isdir(folder_path)}")
# 输出：'my_folder' 是一个目录吗？ True (如果 'my_folder' 确实存在且是目录)

# 2. 判断一个存在的文件
file_path = 'my_file.txt'
print(f"'{file_path}' 是一个目录吗？ {os.path.isdir(file_path)}")
# 输出：'my_file.txt' 是一个目录吗？ False (因为它是一个文件)

# 3. 判断一个不存在的路径
non_existent_path = 'non_existent_folder'
print(f"'{non_existent_path}' 是一个目录吗？ {os.path.isdir(non_existent_path)}")
# 输出：'non_existent_folder' 是一个目录吗？ False (因为它不存在)

# 4. 判断你的 Anno 1800 mods 文件夹
anno_mods_path = r'E:\SteamLibrary\steamapps\common\Anno 1800\mods'
print(f"'{anno_mods_path}' 是一个目录吗？ {os.path.isdir(anno_mods_path)}")
