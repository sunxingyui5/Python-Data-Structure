class Node:
    def __init__(self ,data):      #初始化结点函数
        self.data = data
        self.next = None

class SingleLinkList:
    def __init__(self):      #初始化头结点函数
        self.head = Node(None)

    def CreateSingleLinkedList(self):     #创建单链表函数
        print("********************************************")
        print("*请输入数据后按回车键确认，若想结束请输入“#”。*")
        print("********************************************")
        cNode = self.head
        Element = input("请输入当前结点的值：")
        while Element != "#":
            nNode = Node(int(Element))
            cNode.next = nNode
            cNode = cNode.next
            Element = input("请输入当前结点的值：")

    def InsertElementInTail(self):        #尾端插入元素函数
        Element = (input("请输入待插入结点的值："))
        if Element == "#":
            return
        cNode = self.head
        nNode = Node(int(Element))
        while cNode.next != None:
            cNode = cNode.next
            cNode.next = nNode

    def InsertElementInHead(self):       #首端插入元素函数
        Element = input("请输入待插入点的值：")
        if Element == "#":
            return
        cNode = self.head
        nNode = Node(int(Element))
        nNode.next = cNode.next
        cNode.next = nNode

    def FindElement(self):      #查找指定元素并返回其位置的函数
        Pos = 0
        cNode = self.head
        key = int(input("请输入想要查找的元素值："))
        if self.IsEmpty():
            print("当前链表为空！")
            return
        while cNode.next != None and cNode.data != key:
            cNode = cNode.next
            Pos += 1
            if cNode.data == key:
                print("查找成功，值为",key,"的结点位于该链表的第",Pos,"个位置。")
            else:
                print("查找失败！当前链表中不存在值为",key,"的元素")

    def IsEmpty(self):       #判断单链表是否为空函数
        if self.GetLength() == 0:
            return True
        else:
            return False

    def GetLength(self):        #获取单链表长度函数
        cNode = self.head
        length = 0
        while cNode.next != None:
            length += 1
            cNode = cNode.next
            return length

    def DeleteElement(self):     #删除元素函数
        dElement = int(input("请输入待删除结点的值："))
        cNode = self.head
        pNode = self.head
        if self.IsEmpty():
            print("当前链表为空！")
            return
        while cNode.next != None and cNode.data != dElement:
            pNode = cNode
            cNode = cNode.next
        if cNode.data == dElement:
            pNode.next = cNode.next
            del cNode
            print("成功删除含有元素",dElement,"的结点")
        else:
            print("删除失败！当前链表中不存在含有元素",dElement,"的结点")

    def TravelseElement(self):      #遍历单链表函数
        cNode = self.head
        if cNode.next == None:
            print("当前链表为空！")
            return
        while cNode != None:
            cNode = cNode.next
            self.VisitElement(cNode)

    def VisitElement(self ,tNode):      #输出单链表某一元素函数
        if tNode != None:
            print(tNode.data,"->",end=' ')
        else:
            print("None")
