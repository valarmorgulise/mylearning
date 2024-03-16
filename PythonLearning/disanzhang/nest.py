print("welcome to my zoom")
if int(input("Plase input your height: ")) > 120:
    print("your height is more than 120cm, no free")
    print("if your vip level more the 3, you can play for free")

    if int(input("Please tell me your vip level: ")) > 3:
        print("Congrition you, your vip level is more than 3, your can play for free!")
    else:
        print("Sorry, you need to buy ticket 10  yuan.")

else:
    print("Welcome to little frient, you can play for free!!!")
