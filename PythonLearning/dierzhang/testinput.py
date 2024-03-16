user_name = input("请输入用户名称")
user_type= input("请输入用户类型")
print(f"您好， {user_name}, 您是尊贵的: {user_type}用户， 欢饮您的光临.")
print("您好，%s, 您是尊贵的: %s用户， 欢饮您的光临." % (user_name, user_type))
