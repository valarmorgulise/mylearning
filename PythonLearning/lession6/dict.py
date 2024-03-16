# 定义字典
my_dict1 = {"wanglihuong": 99, "yangyubing": 91, "xupeng": 90}
my_dict2 = {}
my_dict3 = dict()

print(f"字典1的内容是:{my_dict1}, 类型: {type(my_dict1)}")
print(f"字典2的内容是:{my_dict2}, 类型: {type(my_dict2)}")
print(f"字典3的内容是:{my_dict3}, 类型: {type(my_dict3)}")

my_dict1 = {"yangyubing": 99, "yangyubing": 91, "xupeng": 90}
print(f"重复key的字典内容是:{my_dict1}")

my_dict2 = {"wanglihuong": 99, "yangyubing": 91, "xupeng": 90}
score = my_dict2["wanglihuong"]
print(score)

# 定义嵌套字典
stu_score_dict = {
    "yangyubing":{
        "chinese": 77,
        "math": 87,
        "english": 99
    }, "xupeng":{
        "chinese": 88,
        "math": 86,
        "english": 55 
    }, "linhang":{
        "chinese": 77,
        "math": 87,
    "english": 99
    }
}

print(f"student information: {stu_score_dict}")

score = stu_score_dict["yangyubing"]["chinese"]
print(f"yangyubingshi:{score}")
        
# 新增元素
my_dict1 = {"wanglihuong": 99, "yangyubing": 91, "xupeng": 90}
my_dict1["linchuancong"] = 66
print(f"新增后的结果{my_dict1}")
# 更新元素
my_dict1["xupeng"] = 53
print(f"更新后的结果{my_dict1}")
# 删除元素
score = my_dict1.pop("linchuancong")
print(f"字典中被移除了一个元素, 结果:{my_dict1}, 林春从的考试分数是：{score}")

# 清空元素
my_dict1.clear()
print(f"字典被顶空了，内容是{my_dict1}")

my_dict1 = {"wanglihuong": 99, "yangyubing": 91, "xupeng": 90}
keys = my_dict1.keys()
print(f"字典的全部keys是:{keys}")
# 遍历字典
for key in keys:
    print(f"key:{key}")
    print(f"value:{my_dict1[key]}")

for key in my_dict1:
    print(f"key:{key}")
    print(f"value:{my_dict1[key]}")

# 统计字典内的元素数量
num = len(my_dict1)
print(f"num = {num}")

