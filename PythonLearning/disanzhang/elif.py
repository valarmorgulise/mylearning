
height = int(input("Please input your height(cm): "))
vip_level = int(input("Please input your VIP Level(1-5): "))

if height < 120:
    print("Your height is no more than 120cm, your can play for free")
elif vip_level > 3:
    print("vip is more than 3, you can play for free")
else: 
    print("I am sorry, Your condition is no logger, you need to buy ticket 10 yuan")
