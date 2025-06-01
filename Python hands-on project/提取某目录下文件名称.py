import os

def get_folder_names(directory_path):
    """
    提取指定目录下所有一级子文件夹的名字。

    Args:
        directory_path (str): 要扫描的目录路径。

    Returns:
        list: 包含所有文件夹名字的列表。如果目录不存在，则返回空列表。
    """
    folder_names = []
    # 检查路径是否存在且是一个目录
    if not os.path.isdir(directory_path):
        print(f"错误：路径 '{directory_path}' 不存在或不是一个有效的目录。")
        return folder_names

    # 遍历目录下的所有项目
    for item_name in os.listdir(directory_path):
        # 拼接完整路径
        item_path = os.path.join(directory_path, item_name)
        
        # 判断是否是文件夹
        if os.path.isdir(item_path):
            folder_names.append(item_name)
            
    return folder_names

#以我steam目录下的1800MOD文件夹为例子

target_directory = r'E:\SteamLibrary\steamapps\common\Anno 1800\mods' 


print(f"正在提取目录 '{target_directory}' 下的文件夹名字...")

# 调用函数来获取文件夹名字列表
folders = get_folder_names(target_directory)

if folders:
    print("找到的文件夹有：")
    for folder_name in folders:
        print(f"- {folder_name}")
else:
    print("该目录下没有找到任何文件夹。")
