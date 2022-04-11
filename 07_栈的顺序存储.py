class SequenceStack:
    def __init__(self):              #初始化栈函数
        self.MaxStrackSize = 10
        self.s = [None for x in range(0,self.MaxStrackSize)]
        self.top = -1

    def IsEmptyStrack(self):         #判断是否为空的函数
        if self.top == -1:
            iTop = True
        else:
            iTop = False
        return iTop

    def PushStrack(self ,x):            #进栈函数
        if self.top < self.MaxStrackSize - 1:
            self.top = self.top + 1
            self.s[self.top] = x
        else:
            print("栈满")
            return

    def PopStrack(self):                #元素出栈的函数
        if self.IsEmptyStrack():
            print("栈为空")
            return
        else:
            iTop = self.top
            self.top = self.top - 1
            return self.s[iTop]

    def GetTopStrack(self):            #获取栈顶元素函数
        if self.IsEmptyStrack():
            print("栈为空")
            return
        else:
            return self.s[self.top]

    def StrackTraverse(self):          #遍历栈内元素函数
        if self.IsEmptyStrack():
            print("栈为空")
            return
        else:
            for i in range(0,self.top + 1):
                print(self.s[i],end='\t')

    def CreateStrackByInput(self):     #将用户输入的数据元素进栈的函数
        data = input("请输入元素（继续输入请按回车键，结束请输入“#”）：")
        while data != '#':
            self.PushStrack(data)
            data = input("请输入元素：")

# ss = SequenceStack()
# ss.CreateStrackByInput()
# print("栈内元素为：",end=' ')
# ss.StrackTraverse()
# print(ss.IsEmptyStrack())