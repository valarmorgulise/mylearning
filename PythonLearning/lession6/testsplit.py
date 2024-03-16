str = "itheima itcast boxuegu"

count = str.count("it")

print(f"字符串{str}中有{count}个”it字符")

new_str = str.replace(" ", "|")
print(f"字符chuan{str}替换后的新字符串为{new_str}")

new_str1 = new_str.split("|")
print(f"{new_str}分割后的列表为{new_str1}")
