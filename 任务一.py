#任务一
# 1-1
# list=[1,2,3,4,5,6,7,8,9,10]
# a=0
# for i in range(10):
#     a=list[i-1]+a
#     if i==9:
#          print(a)

#1-2
# print("请输入十个数")
# while True:
#     q =int(input("请输入第1个数"))
#     w = int(input("请输入第2个数"))
#     e = int(input("请输入第3个数"))
#     t = int(input("请输入第4个数"))
#     y = int(input("请输入第5个数"))
#     u = int(input("请输入第6个数"))
#     o = int(input("请输入第7个数"))
#     p = int(input("请输入第8个数"))
#     a = int(input("请输入第9个数"))
#     s = int(input("请输入第10个数"))
#     H=q+w+e+t+y+u+o+p+a+s
#     P=(q+w+e+t+y+u+o+p+a+s)/10
#     max = q
#     if e > max:
#         max = e
#     if t > max:
#         max = t
#     if y > max:
#         max = y
#     if u > max:
#         max = u
#     if o > max:
#         max = o
#     if p > max:
#         max = p
#     if a > max:
#         max = a
#     if s > max:
#         max = s
#     print("最大值为", max)
#     print("十个数的和为",int(H))
#     print("十个数的平均数为",round(P,2))
#     break

#1-3
# import random
# randint=random.randint(50,150)
# print(randint)

#1-4
# while True:
#     a = int(input("边"))
#     b = int(input("边"))
#     c = int(input("边"))
#     if a+b>c and a+c>b and c+b>a and c-a<b and a-b<c and b-c<b:
#          print("是三角形")
#     else:
#         print("输入的三条边不构成三角形")
#         break
#     if  a==b==c:
#         print("等边三角形")
#     elif a==b:
#         print("等腰三角形")
#     elif a*a+b*b==c*c or a*a+c*c==b*b or c*c+b*b:
#         print("直角三角形")
#     else:
#         print("普通三角形")

#1-5
# A=56
# B=78
# C=0
# C=B-A
# A=A+C
# B=B-C
# print("A=",A)
# print("B=",B)

#1-6
# i=3
# while True:
#     a=("root")
#     b=("admin")
#     N=input("请输入用户名：")
#     M=input("请输入密码：")
#     if N==a and M==b:
#         print("登录成功")
#     else:
#         i=i-1
#         print("登录失败")
#     if i==0:
#         print("密码输入错误超过3次系统锁定")
#         break

#1-7
# print("      *")
# print("     * *")
# print("    * * *")
# print("   * * * * ")
# print("  * * * * * ")
# print(" * * * * * * ")
# print("* * * * * * * ")


#1-8
# num=int(input("请输入一个数"))
# i=0
# while i<num:
#     j=1
#     while j<=i+1:
#         print("%d*%d=%d"%(j,i+1,j*(i+1)),end="   ")
#         j+=1
#     print()
#     i+=1

#1-9
# for i in range(9,0,-1):
#     for j in range(1, i+1):
#         print('{}x{}={}\t'.format(j, i, i*j), end='')
#     print()

#1-10
# h=20
# w=3
# e=2
# s=(h-w)/1+1
# print(int(s))

# 1-11
# while True:
#     name=input("输入一个变量名:")
#     if name.isalpha():
#         print("变量名合法")
#     else:
#         print("变量名不合法")
#     break

#1-12
# import random
# randint=random.randint(1, 20)
# i=5
# print("欢迎来到数字猜猜猜，猜对了加3个金币猜错了减一个金币")
# while i>=1:
#     print("您还有%d次机会"%i)
#     num=int(input("请输入您猜的数字"))
#     if num>20 or num <0:
#         print("请输入1~20的数")
#     else:
#         if num == randint:
#             print("恭喜你猜对了金币加3,答案为:", randint)
#             i = i + 2
#             randint = random.randint(1, 20)
#             continue
#         elif num > randint:
#             print("猜大了,继续猜金币减一")
#             i = i - 1
#         elif num < randint:
#             print("猜小了,继续猜金币减一")
#             i = i - 1
#         if i == 1:
#             print("你只有一次机会喽")
#         if i == 0:
#             print("金币为0,请充值答案为:", randint)


#1-13
# num=int(input("输入一个数："))
# shu=1
# for i in range(1,num+1):
#     shu=shu*i
# print("数字",num,"的阶乘",shu)