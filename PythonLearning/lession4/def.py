str1 = "iterere"
str2 = "itcast"
str3 = "python"

count = 0
for i in str1:
    count += 1 
print(f"str {str1}'s length: {count}")

count = 0
for i in str2:
    count += 1 
print(f"str {str2}'s length: {count}")

count = 0
for i in str3:
    count += 1 
print(f"str {str3}'s length: {count}")

def my_len(data):
    count = 0 
    for i in data:
        count += 1 
    print(f"str{data}'s length: {count}")

my_len(str1)
my_len(str2)
my_len(str3)
