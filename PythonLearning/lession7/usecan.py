
def user_info(name, age, gender):
    print(f"姓名是:{name}, 年龄是:{age}, 性别是:{gender}")

user_info("养育并", 18, '男')

user_info(name = '小徐', age = 11, gender = '女')
user_info(age = 10, gender = "女", name = '潇潇')
user_info('天天', gender = '女', age = 10)

# 缺省函数
def user_info2(name, age, gender = '男'):
    print(f"姓名是:{name}, 年龄是:{age}, 性别是:{gender}")

user_info2('xiaotian', 13)

# 不定长， 位置不定长
# 不定长的形式参数会作为元组存在，接受不定长数量的参数传入
def user_info3(*args):
    print(f"args参数的类型是: {type(args)}, 内容是:{args}")

user_info3(1, 2, 3, '小明', '男孩')

def user_info4(**kwargs):
    print(f"args参数的类型是: {type(kwargs)}, 内容是:{kwargs}")
user_info4( name = '小明', age = 11, gender = '男孩')
