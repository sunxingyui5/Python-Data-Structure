class CircularSequenceQueue:
    def __init__(self):               #初始化循环队列函数
        self.MaxQueueSize = 10
        self.s = [None for x in range(0,self.MaxQueueSize)]
        self.front = 0
        self.rear = 0

    def IsEmptyQueue(self):           #判断循环队列是否为空的函数
        if self.front == self.rear:
            iQueue = True
        else:
            iQueue = False
        return iQueue

    def EnQueue(self ,x):             #元素进队的函数
        if (self.rear + 1) % self.MaxQueueSize != self.front:
            self.rear = (self.rear + 1) % self.MaxQueueSize
            self.s[self.rear] = x
            print("当前进队元素为：",x)
        else:
            print("队列已满，无法进队")
            return

    def DeQueue(self):               #元素出队的函数
        if self.IsEmptyQueue():
            print("队列为空，无法出队")
            return
        else:
            self.front = (self.front + 1) % self.MaxQueueSize
            return self.s[self.front]

    def CreateQueueByInput(self):    #将用户输入的元素进队的函数
        data = input("请输入元素（继续请按回车键，结束请输入“#”）：")
        while data != '#':
            self.EnQueue(data)
            data = input("请输入元素：")

    def OutPutQueue(self):          #输出元素函数
        a = []
        if self.IsEmptyQueue():
            print("队列为空")
            return
        else:
            for i in range(1,self.rear+1):
                a.append(self.s[i])
        print("当前队列为：",a)

#Test
sq = CircularSequenceQueue()
sq.CreateQueueByInput()
sq.OutPutQueue()