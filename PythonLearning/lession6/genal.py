my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_str = "abcdefg"
my_set = {1, 2, 3, 4, 5}
my_dict = {"key1": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5}

print(f"列表 元素个数有: {len(my_list)}")
print(f"元组 元素个数有: {len(my_tuple)}")
print(f"字符串 元素个数有: {len(my_str)}")
print(f"集合 元素个数有: {len(my_set)}")
print(f"字典 元素个数有: {len(my_dict)}")

# max最大元素
print(f"列表 最大的元素有: {max(my_list)}")
print(f"元组 最大的元素有: {max(my_tuple)}")
print(f"字符串 最大的元素有: {max(my_str)}")
print(f"集合 最大的元素有: {max(my_set)}")
print(f"字典 最大的元素有: {max(my_dict)}")

# min最小元素
print(f"列表 最小的元素是: {min(my_list)}")
print(f"元组 最小的元素是: {min(my_tuple)}")
print(f"字符串 最小的元素是: {min(my_str)}")
print(f"集合 最小的元素是: {min(my_set)}")
print(f"字典 最小的元素是: {min(my_dict)}")

# 类型转换: 容器转列表
print(f"列表转列表的结果是: {list(my_list)}")
print(f"元组转列表的结果是: {list(my_tuple)}")
print(f"字符串转列表的结果是: {list(my_str)}")
print(f"集合转列表的结果是: {list(my_set)}")
print(f"字典转列表的结果是: {list(my_dict)}")

# 类型转换: 容器转
print(f"列表转元组的结果是: {tuple(my_list)}")
print(f"元组转元组的结果是: {tuple(my_tuple)}")
print(f"字符串转元组的结果是: {tuple(my_str)}")
print(f"集合转元组的结果是: {tuple(my_set)}")
print(f"字典转元组的结果是: {tuple(my_dict)}")

# 类型转换: 容器转字符串
print(f"列表转字符串的结果是: {str(my_list)}")
print(f"转字符串的结果是: {str(my_tuple)}")
print(f"字符串转字符串的结果是: {str(my_str)}")
print(f"集合转字符串的结果是: {str(my_set)}")
print(f"字典转字符串的结果是: {str(my_dict)}")

# 类型转换: 容器转集合
print(f"列表转集合的结果是: {set(my_list)}")
print(f"转集合的结果是: {set(my_tuple)}")
print(f"字符串转集合的结果是: {set(my_str)}")
print(f"集合转集合的结果是: {set(my_set)}")
print(f"字典转集合的结果是: {set(my_dict)}")

my_list = [2, 1, 4, 3, 5]
my_tuple = (1, 4, 5, 2, 3)
my_str = "abcdefg"
my_set = {1, 5, 4, 3, 2}
my_dict = {"key1": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5}
# 进行容器的排序
print(f"列表对象的排序结果是:{sorted(my_list)}")
print(f"元组对象的排序结果是:{sorted(my_tuple)}")
print(f"字符串对象的排序结果是:{sorted(my_str)}")
print(f"集合对象的排序结果是:{sorted(my_set)}")
print(f"字典对象的排序结果是:{sorted(my_dict)}")

print(f"列表对象的反向排序结果是:{sorted(my_list, reverse = True)}")
print(f"元组对象的反向排序结果是:{sorted(my_tuple, reverse = True)}")
print(f"字符串对象反向的排序结果是:{sorted(my_str, reverse = True)}")
print(f"集合对象的反向排序结果是:{sorted(my_set, reverse = True)}")
print(f"字典对象的反向排序结果是:{sorted(my_dict, reverse = True)}")
