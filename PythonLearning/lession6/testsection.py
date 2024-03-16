str = "万过心月, 员序程马黑来, nohpojio"
my_str = str[::-1][11:16]
print(f"方式结果:{my_str}")
result2 = str[6:11][::-1]
print(f"方式结果:{result2}")
result3 = str.split(",")[1].replace("来", "")[::-1]
print(f"方式结果:{result3}")


