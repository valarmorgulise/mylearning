my_set = {"hello", "world", "youare", "hello", "world", "youare"}
my_set_empty = set()

print(f"my_set的内容是:{my_set}, 类型是:{type(my_set)}")
print(f"my_set_empty的内容是:{my_set_empty}, 类型是:{type(my_set_empty)}")

# 添加新元素
my_set.add("Python")
my_set.add("hello")
print(f"添加元素后结果是: {my_set}")

# 移除元素
my_set.remove("youare")
print(f"移除yourare后结果是:{my_set}")

my_set = {"hello", "world", "youare"}
element = my_set.pop()
print(f"取出元素{element}后：{my_set}")

my_set.clear()
print(my_set)

#取两个元素的差集
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.difference(set2)
print(f"取出差集后的结果是:{set3}")
print(f"取差集后， 原有set1的内容: {set1}")
print(f"取差集后， 原有set2的内容: {set2}")

set1 = {1, 2, 3}
set2 = {1, 5, 6}
set1.difference_update(set2)
print(f"取差集后， 原有set1的内容: {set1}")
print(f"取差集后， 原有set2的内容: {set2}")

# 合并
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.union(set2)
print(f"合并集后的结果是:{set3}")
print(f"合并集后， 原有set1的内容: {set1}")
print(f"合并集后， 原有set2的内容: {set2}")

