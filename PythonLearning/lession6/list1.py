mylist = ["itcast", "itheima", "python"]

index = mylist.index("itheima")
print(f"itheima在列表中的下摆哦是:{index}")

index = mylist.index("python")
print(f"python在列表中的下摆哦是:{index}")

mylist[0] = "helo"
print(f"被修改后的元素的值是，结果是:{mylist}")

mylist.insert(1, "best")
print(f"列表插入元素后， 结果为:{mylist}")

mylist.append("yangyubing")
print(f"猎豹增加元素后, 结果为:{mylist}")

mylist2 = [1, 2, 3]
mylist.extend(mylist2)
print(f"列表在追加了一个新的列表后，结果是: {mylist}")

mylist = ["itcast", "itheima", "python"]
del mylist[2]
print(f"咧白哦删除元素后，结果是：{mylist}")

mylist = ["itcast", "itheima", "python"]
element = mylist.pop(2)
print(f"通过pop方法取到的元素是:{element}")
print(f"咧白哦删除元素后，结果是：{mylist}")

mylist = ["itcast", "itheima", "python", "itheima", "python"]
mylist.remove("python")
print(f"remove {mylist}")

mylist = ["itcast", "itheima", "python", "itheima", "python"]
mylist.clear()
print(f"列表被清空了，结果是{mylist}")

mylist = ["itcast", "itheima", "python", "itheima", "python"]
count = mylist.count("itheima")
print(f"列表中itheima数量为{count}")
print(len(mylist))

