class DoubleLinkedNode:
    def __init__(self ,data):            #初始化结点函数
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:                  #初始化头结点函数
    def __init__(self):
        self.head = DoubleLinkedNode(None)

    def CreateCircularDoubleLinkedList(self):   #创建循环双链表函数
        print("********************************************")
        print("*请输入数据后按回车键确认，若想结束请输入“#”。*")
        print("********************************************")
        data = input("请输入元素：")
        cNode = self.head
        while data != '#':
            nNode = DoubleLinkedNode(int(data))
            cNode.next = nNode
            nNode.prev = cNode
            nNode.next = self.head
            self.head.prev = nNode
            cNode = cNode.next
            data = input("请输入元素：")

    def InsertElementInTail(self):              #尾端插入元素函数
        Element = input("请输入待插入结点的值：")
        if Element == '#':
            return
        nNode = DoubleLinkedNode(int(Element))
        cNode = self.head
        while cNode.next != self.head:
            cNode = cNode.next
        cNode.next = nNode
        nNode.prev = cNode
        nNode.next = self.head
        self.head.prev = nNode

    def InsertElementInHead(self):            #首端插入元素函数
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

    def DeleteElement(self):                 #删除元素函数
        dElement = int(input("请输入待删除结点的值："))
        cNode = self.head
        pNode = self.head
        if self.IsEmpty():
            print("当前双链表为空！")
            return
        while cNode.next != self.head and cNode.data != dElement:
            pNode = cNode
            cNode = cNode.next
        if cNode.data == dElement:
            qNode = cNode.next
            pNode.next = qNode
            qNode.prev = pNode
            del cNode
            print("成功删除含有元素",dElement,"的结点")
        else:
            print("删除失败！循环双链表中不存在含有元素",dElement,"的结点\n")

    def IsEmpty(self):  # 判断双链表是否为空函数
        if self.GetLength() == 0:
            return True
        else:
            return False