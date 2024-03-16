
def check_health(x):
    print("欢迎来到这里！请出示您的健康吗以及72小时核算证明，并配合测量体温!")
    if x <= 37.5:
        print(f"提问测量中，您的提问是: {x}度, 体温正常请进！")
    else:
        print(f"体温测量中，您的提问是: {x}度, 需要隔离！")
        

check_health(36.3)
check_health(39.3)
