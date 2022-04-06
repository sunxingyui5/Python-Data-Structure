class Node:
    def __init__(self ,data):
        self.data = data
        self.next = None

class CircularSingleLinkedList:
    def __init__(self):
        self.head = Node(None)

    def CreateCricularSingleLinkedList(self):          #创建循环单链表函数
        print("********************************************")
        print("*请输入数据后按回车键确认，若想结束请输入“#”。*")
        print("********************************************")
        data = input()
        cNode = self.head
        while data != "#":
            nNode = Node(int(data))
            cNode.next = nNode
            nNode.next = self.head
            cNode = cNode.next
            data = input("请输入结点的值：")

    def InsertElementInTail(self):        #尾端插入函数
        Element = input("请输入待插入结点的值：")
        if Element != '#':
            return
        cNode = self.head
        nNode = Node(int(Element))
        while cNode.next != self.head:
            cNode = cNode.next
        cNode.next = nNode
        nNode.next = self.head

    def InsertElementInHead(self):           #首端插入函数
        Element = input("请输入待插入结点的值：")
        if Element != "#":
            return
        cNode = self.head
        nNode = Node(int(Element))
        nNode.next = cNode.next
        cNode.next = nNode

    def DeleteElement(self):                #删除元素函数
        dElement = int(input('请输入待删除结点的值：'))
        cNode = self.head
        pNode = self.head
        if self.IsEmpty():
            print("当前循环列表为空！")
            return
        while cNode.next != self.head and cNode.data != dElement:
            pNode = cNode
            cNode = cNode.next
        if cNode.data == dElement:
            pNode.next = cNode.next
            del cNode
            print("成功删除含有元素",dElement,"的结点")
        else:
            print("删除失败！单链表中不存在含有元素",dElement,"的结点\n")

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