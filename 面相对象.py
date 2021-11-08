# class beer:
#     # L = input("请输入长度：")
#     # V = input("请输入容积：")
#     # C = input("请输入颜色：")
#     # T = input("请输入材质：")
#     __L =0
#     __V =0
#     __C = ""
#     __T = ""
#     def setL(self,L):
#         if L>50 or L<=5:
#             print("错误")
#         else:
#             self.__L=L
#     def getL(self):
#         return self.__L
#     def setV(self,V):
#         if V>2000 or V<=0:
#             print("错误")
#         else:
#             self.__V=V
#     def getV(self):
#         return self.__V
#     def setC(self,C):
#         if C=="黑色" or C=="白色":
#             self.__C=C
#         else:
#             self.__C=C
#             print("没有这种颜色")
#     def getC(self):
#         return self.__C
#     def setT(self,T):
#         if T=="塑料" or T=="铁":
#             self.__T = T
#         else:
#             print("没有这种材质")
#     def getT(self):
#         return self.__T
#
#
#     def filling(self):
#         print("我是个长",self.__L,"cm","可以装",self.__V,"L水","颜色是",self.__C,"材质是",self.__T,"的杯子")
#
# b = beer()
# b.setL(int(input("请输入长度：")))
# b.setV(int(input("请输入容积：")))
# b.setC(input("请输入颜色："))
# b.setT(input("请输入材质："))
# b.filling()


class computer:
    __size = 0
    __many = 0
    __RAM = ""
    __time = 0
    def setsize(self,size):
        if size > 128 or size <4:
            print("错误")
        else:
            self.__size = size
    def getsize(self):
        return self.__size
    def setmany(self,many):
        if many>100000 or many<=0:
            print("错误")
        else:
            self.__many = many
    def getmany(self):
        return self.__many
    def setRAM(self,RAM):
        if RAM=="i3" or RAM=="i4" or RAM=="i5":
            self.__RAM=RAM
        else:
            print("错误")
    def getRAM(self):
        return self.__RAM
    def settime(self,time):
        if time>24 or time<=0:
            print("错误")
        else:
            self.__time=time
    def gettime(self):
        return self.__time
    def type(self,type):
        print("可以在",self.__size,"寸",self.__many,"块",self.__RAM,"型号的电脑","上",type)
    def playgame(self,playgame):
        print("可以在",self.__size,"寸",self.__many,"块",self.__RAM,"型号的电脑","上打",playgame)
    def playvideo(self,video):
        print("可以在",self.__size,"寸",self.__many,"块",self.__RAM,"型号的电脑","上看",video)
p = computer()
p.setsize(16.5)
p.settime(24)
p.setmany(10000)
p.setRAM("i5")
p.type("打字")
p.playgame("英雄联盟")
p.playvideo("哔哩哔哩")