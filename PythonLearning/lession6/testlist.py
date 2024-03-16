list = [21, 25, 21, 23, 22, 20]
list.append(31)
list1 = [29, 33, 30]
list.extend(list1)
num = list[0]
print("第一个元素为%d" % num)
num = list[-1]
print("最后一个元素为%d" % num)
index = list.index(31)
print("31 在列表中的下标位置为%d" % index)
print(list)
