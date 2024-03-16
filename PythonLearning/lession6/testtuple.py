student = ('周杰伦', 11, ['football', 'music'])

index = student.index(11)
print(f"年龄的所在的下标位置{index}")

print(f"学生的姓名为{student[0]}")

del student[2][0]
print(f"该百年原来的元组内容为{student}")

student[2].append('coding')
print(f"该百年原来的元组内容为{student}")

