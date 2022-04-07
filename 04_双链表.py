class DoubleLinkedNode:
    def __init__(self ,data):            #初始化结点函数
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:                  #初始化头结点函数
    def __init__(self):
        self.head = DoubleLinkedNode(None)

    def CreateDoubleLinkedList(self):    #创建双链表函数
        print("********************************************")
        print("*请输入数据后按回车键确认，若想结束请输入“#”。*")
        print("********************************************")
        data = input("请输入元素：")
        cNode = self.head
        while data != '#':
            nNode = DoubleLinkedNode(int(data))
            cNode.next = nNode
            nNode.prev = cNode
            cNode = cNode.next
            data = input("请输入元素：")

    def InsertElementInTail(self):       #尾端插入函数
        Element = input("请插入待插入结点的值：")
        if Element == '#':
            return
        nNode = DoubleLinkedNode(int(Element))
        cNode = self.head
        while cNode.next != None:
            cNode = cNode.next
        cNode.next = nNode
        nNode.prev = cNode

    def InsertElementInHead(self):       #首端插入元素函数
        Element = input("请输入待插入结点的值：")
        if Element == '#':
            return
        cNode = self.head.next
        pNode = self.head
        nNode = DoubleLinkedNode(int(Element))
        nNode.prev = pNode
        pNode.next = nNode
        nNode.next = cNode
        cNode.prev = nNode

    def DeleteElement(self):            #删除元素函数
        dElement = int(input("请输入待删除结点的值："))
        cNode = self.head
        pNode = self.head
        if self.IsEmpty():
            print("当前双链表为空！")
            return
        while cNode.next != None and cNode.data != dElement:
            pNode = cNode
            cNode = cNode.next
        if cNode.data == dElement:
            if cNode.next == None:
                pNode.next = None
                del cNode
                print("成功删除含有元素",dElement,"的结点！\n")
            else:
                qNode = cNode.next
                pNode.next = qNode
                qNode.prev = pNode
                del cNode
                print("成功删除含有元素",dElement,"的结点！\n")
        else:
            print("删除失败！双链表中不存在含有元素",dElement,"的结点！\n")

    def TraversDoubleLinkedList(self):  #遍历双链表函数
        cNode = self.head
        print("按next域遍历带头结点双链表：")
        if self.IsEmpty():
            print("当前双列表为空！")
            return
        while cNode.next != None:
            cNode = cNode.next
            self.VisitElementByNext(cNode)
        print("None")

    def VisitElementByNext(self ,tNode):  #按next域输出某一元素函数
        if tNode != None:
            print(tNode.data,"->",end=' ')

    def IsEmpty(self):  # 判断双链表是否为空函数
        if self.GetLength() == 0:
            return True
        else:
            return False

    def GetLength(self):  # 获取双链表长度函数
        cNode = self.head
        length = 0
        while cNode.next != None:
            length += 1
            cNode = cNode.next
            return length