


f = open("./my.txt", "r", encoding = "UTF-8")

print(type(f))

# print(f"读取10个字节的结果:{f.read(10)}")
# print(f"read方法读取全部的内容是: {f.read()}")

# 读取文件的额全部行，封装到列表中
# lines = f.readlines()
# print(f"lines对象的类型:{type(lines)}")
# print(f"lines对象的内容是: {lines}")

for line in f:
    print(f"每一行数据是:{line}")
