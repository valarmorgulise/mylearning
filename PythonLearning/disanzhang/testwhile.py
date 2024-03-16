import random 
num = random.randint(1, 100)

count = 0

flag = True 
while flag:
    guess_num = int(input("请输入你要猜测的数字:"))
    count += 1
    if guess_num == num:
        print("猜中了")
        flag = False
    else:
        if guess_num > num:
            print("尼采的打了")
        else:
            print("你猜的小了")

print("你总共猜了{count}次")
