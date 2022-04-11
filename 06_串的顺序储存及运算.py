class StringList:
    def __init__(self):                #初始化串的函数
        self.MaxStringSize = 256
        self.chars = ""
        self.length = 0

    def IsEmptyString(self):               #判断是否为空的函数
        if self.length == 0:
            IsEmpty = True
        else:
            IsEmpty = False
        return IsEmpty

    def CreateString(self):                #创建一个串的函数
        stringSH = input("请输入字符串，按回车键结束输入：")
        if len(stringSH) > self.MaxStringSize:
            print("输入的字符串序列超过分配的存储空间，超过的部分无法存入当前串中。")
            self.chars = stringSH[:self.MaxStringSize]
        else:
            self.chars = stringSH

    def StringConcat(self ,strSrc):        #串连接的函数
        lengthSrc = strSrc.length
        stringSrc = strSrc.chars
        if lengthSrc + len(strSrc.chars) <= self.MaxStringSize:
            self.chars = self.chars + stringSrc
        else:
            print("两个字符串连接后的长度超过分配的内存，超过的部分无法显示。")
            size = self.MaxStringSize - len(self.chars)
            self.chars = self.chars + stringSrc[0:size]
        print("连接后的字符串为：",self.chars)

    def SubString(self ,iPos ,length):    #从指定位置开始获取指定长度字串的函数
        if iPos > len(self.chars) - 1 or iPos < 0 or length <1 or (length + iPos) > len(self.chars):
            print("无法获取子串。")
        else:
            substr = self.chars[iPos:iPos + length]
            print("获取的字串为：",substr)