r = open("./bill.txt", "r", encoding="UTF-8")

new_file = open("./bill.txt.bak", "w", encoding="UTF-8")

for line in r:
    line = line.strip()
    if line.split(",")[4] == "测试":
        continue 
    new_file.write(line)
    new_file.write("\n")

r.close()
new_file.close()

