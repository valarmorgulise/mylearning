import random 
sum = 10000

for i in range(1, 20):
    per = random.randint(1, 10)
    if per < 5:
        print(f"员工{i}, 绩效{per}, 低于5， 不发工资，下一位")
        continue
    if sum >= 1000:
        sum -= 1000
        print(f"向员工{i}发送工资1000元， 账户元和还剩余{sum}元")
    else:
        print(f"余额不足，当前余额:{sum}元, 不足以发工资, 不发了，写个月再来")
        break
