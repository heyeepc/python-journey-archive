with open("文件名", "r", encoding="utf-8") as file:
    contents = file.read()
    print(contents)

with open("C:/Users/yourname/Documents/data.txt", "r") as f:
    content = f.read()

import os
filepath = os.path.join("folder", "subfolder", "file.txt")

from pathlib import Path
filepath = Path("folder") / "subfolder" / "file.txt"
