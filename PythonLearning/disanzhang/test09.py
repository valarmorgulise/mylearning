import random

num = random.randint(1, 10)

guess_num = int(input("Please input your guess num: "))
if guess_num == num:
    print("Congriautiono, 第一次猜中了")
else:
    if guess_num > num:
        print("你猜测的数据大了")
    else:
        print("你猜测的数据xiao了")

    guess_num = int(input("Please input your guess num: "))

    if guess_num == num:
        print("Congriautiono, 第二次猜中了")
    else:
        if guess_num > num:
            print("你猜测的数据大了")
        else:
            print("你猜测的数据xiao了")
