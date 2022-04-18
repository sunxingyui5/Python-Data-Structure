class QueueNode:
    def __init__(self):                #初始化结点的函数
        self.data = None
        self.next = None

class LinkQueue:
    def __init__(self):                #初始化链式队列的函数
        tQueueNode = QueueNode()
        self.front = tQueueNode
        self.rear = tQueueNode

    def IsEmptyQueue(self):            #判断链式队列是否为空的函数
        pass