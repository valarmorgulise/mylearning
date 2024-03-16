
import time
f = open("./test.txt", "w", encoding = "UTF-8")

f.write("Hello World!")
f.flush()
# time.sleep(560000)

f.close()
