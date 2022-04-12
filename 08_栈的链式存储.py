class StackNode:
    def __init__(self):                 #初始化结点的函数
        self.data = None
        self.next = None

class LinkStack:
    def __init__(self):                 #初始化链栈的函数
        self.top = StackNode()

    def IsEmptyStack(self):             #判断链栈是否为空的函数
        if self.top.next == None:
            iTop = True
        else:
            iTop = False
        return iTop

    def PushStack(self ,da):            #进栈的函数
        tStackNode = StackNode()
        tStackNode.data = da
        tStackNode.next = self.top.next
        self.top.next = tStackNode
        print("当前进栈元素为：",da)

    def PopStack(self):                 #出栈的函数
        if self.IsEmptyStack() == True:
            print("栈为空。")
            return
        else:
            tStackNode = self.top.next
            self.top.next = tStackNode.next
            return tStackNode.data

    def GetTopStack(self):             #获得当前栈顶元素的函数
        if self.IsEmptyStack():
            print("栈为空。")
            return
        else:
            return self.top.next.data

    def CreateStackByInput(self):      #将用户输入的数据元素进栈的函数
        data = input("请输入元素（继续输入请按回车键，结束请输入“#”）：")
        while data != '#':
            self.PushStack(data)
            data = input("请输入元素")

#Test
ls = LinkStack()
ls.CreateStackByInput()