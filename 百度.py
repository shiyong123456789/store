# f = open(file="baidu_x_system.log", mode="r+", encoding="utf-8")
# # data = f.read()
# data =  f.readlines()
# print(data)
import re
with open("baidu_x_system.log") as f1:
    message = ""
    for line in f1:
        message+=line
a = re.findall("10.155.24.132",message)
b = re.findall("16.155.34.132",message)
c = re.findall("56.78.35.131",message)
d = re.findall("46.76.185.36",message)
print(len(a))
print(len(b))
print(len(c))
print(len(d))