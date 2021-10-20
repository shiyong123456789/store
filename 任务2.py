import random
randint=random.randint(1, 20)
i=5
print("欢迎来到数字猜猜猜，猜对了加3个金币猜错了减一个金币")
while i>=1:
    print("您还有%d次机会"%i)
    num=int(input("请输入您猜的数字"))
    if num>20 or num <0:
        print("请输入1~20的数")
    else:
        if num == randint:
            print("恭喜你猜对了金币加3,答案为:", randint)
            i = i + 2
            randint = random.randint(1, 20)
            continue
        elif num > randint:
            print("猜大了,继续猜金币减一")
            i = i - 1
        elif num < randint:
            print("猜小了,继续猜金币减一")
            i = i - 1
        if i == 1:
            print("你只有一次机会喽")
        if i == 0:
            print("金币为0,请充值答案为:", randint)