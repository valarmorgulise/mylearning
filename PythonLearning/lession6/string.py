my_str = "itheima and itcast"

#通过下标索引取值
value = my_str[2]
value2 = my_str[-16]
print(f"从字符串{my_str}取下标为2的元素，值是：{value}, 取下标为-16的元素，值是:{value2}")

# index方法
value = my_str.index("and")
print(f"在字符串{my_str}中查找and， 其起始下标是:{value}")

#replace 方法
new_my_str = my_str.replace("it", "santa")
print(f"将{my_str},进行替换后得到:{new_my_str}")

#split 
my_str = "hello python ithemima itcast"
my_str_list = my_str.split(" ")
print(f"将字符串 {my_str}进行split切分后得到{my_str_list}, 类型是{type(my_str_list)}")

# strip
my_str = " itheima and itcast "
print(my_str.strip())

my_str = "12ithima and itcast21"
print(my_str.strip("12"))

#统计字符串中某字符串出现的次数 count 
my_str = "itheima and itcast"
count = my_str.count("it")
print(f"字符串{my_str}中it出现的次数是:{count}")

# 统计字符串的长度

