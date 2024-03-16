
f = open("./word.txt", "r", encoding = "UTF-8")

# lines = f.read()
# count = lines.count("itheima")
# print(f"itheima在文件中出现了:{count} 次")
count = 0
for line in f:
    line = line.strip()
    words = line.split(" ")
    for word in words:
        if word == "itheima":
            count += 1

print(f"itheima出现的次数是:{count}")
