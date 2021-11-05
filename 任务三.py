# print("姓名  年龄 性别  编号  任职公司 薪资 部门编号")
# name=[["曹操","56","男","106","IBM",500,"50"],\
#       ["大乔","19","女","230","微软",501,"60"],\
#       ["小乔","19","女","210","Oracle",600,"60"],\
#       ["许褚","45","男","230","Tencent",700,"10"],]
# #平均工资/年龄
# num=0
# sum=0
# for i in range(len(name)):
#     num+=name[i][5]
#     sum+=int(name[i][1])
# print("平均工资为",num/len(name))
# print("平均年龄为",sum/len(name))
# #添加
# name.append(["刘备","45","男","220","alibaba",500,"30"])
# #统计
# man=0
# woman=0
# a=0
# bumen1=0
# bu2=0
# bu3=0
# bu4=0
# while True:
#     if name[a][6]=="60":
#         bumen1+=1
#     elif name[a][6]=="50":
#         bu2+=1
#     elif name[a][6]=="10":
#         bu3+=1
#     elif name[a][6]=="30":
#         bu4+=1
#     if name[a][2]=="男":
#         man+=1
#         a+=1
#     elif name[a][2]=="女":
#         woman+=1
#         a+=1
#     if man+woman == len(name):
#         break
# print(man,woman)
# print(bumen1,bu2,bu3,bu4)


#3-2
# mofa=[["罗恩","23","35","44",],
#       ["哈利","60","77","68","88","90"],
#       ["赫敏","97","99","89","91","95","90"],
#       ["马尔福","100","85","90"]]
#
# for i in range(len(mofa)):
#     Z=0
#     for j in range(len(mofa[i])):
#         j+=1
#         if j==len(mofa[i]):
#             continue
#         else:
#             Z+=int(mofa[i][j])
#     print(mofa[i][0],"的总成绩为",Z)

#3-3
# num=int(input("请输入一个数："))
# while num !=0:
#     print(num%10)
#     num=num//10


#3-4
# a=[5,2,4,7,9,1,3,5,4,0,6,1,3]
# a.sort()
# print(a)
