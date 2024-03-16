"""
演示tuple元组的定义和操作
"""
# 定义元组
t1 = (1, "Hello", True)
t2 = ()
t3 = tuple()

print(f"t1的类型是: {type(t1)}, 内容是{t1}")
print(f"t2的类型是: {type(t2)}, 内容是{t2}")
print(f"t3的类型是: {type(t3)}, 内容是{t3}")

#定义单个内容
t4 = ("hello")
print(f"t4的类型是: {type(t4)}, 内容是{t4}")

t5 = ((1, 2, 3), (4, 5, 6))
print(f"t5的类型是: {type(t5)}, 内容是{t5}")

#下标所以去除内容
num = t5[1][2]
print(f"从嵌套元组中取出的数据是:{num}")

# index查找方法``
t6 = ("hello", "world", "Python")
index = t6.index("hello")
print(f"在元组6中查找内容的下标是:{index}")

# count统计方法
t7 = ("hello", "world", "Python", "world", "world")
num = t7.count("world")
print(f"在元组t7数量有{num}个")

t8 = ("hello", "world", "Python", "world", "world")
num = len(t8)
print(f"t8元组中的元素有:{num}个")
# 元组的遍历:while 
index = 0
while index < len(t8):
    print(f"元组的元素有: {t8[index]}")
    index += 1
# 元组的遍历: for 
for element in t8:
    print(f"元组的元素有: {element}")

# 修改元组内容

t9 = (1, 2, ["hello", "world"])
print(f"t9的内容是：{t9}")
t9[2][0] = "yangyubing"
t9[2][1] = "xupeng"
print(f"t9的内容是：{t9}")




