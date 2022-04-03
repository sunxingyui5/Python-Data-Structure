class SequenceList:
    def __init__(self):    #初始化顺序表函数
        self.SeqList = []

    def CreateSequenceList(self):     #创建顺序函数表
        print("********************************************")
        print("*请输入数据后按回车键确认，若想结束请输入“#”。*")
        print("********************************************")
        Element = input("请输入元素：")
        while Element != '#':
            self.SeqList.append(int(Element))
            Element = input("请输入元素")

    def FindElement(self):     #查找元素函数
        key = int(input("请输入想要查找的元素值："))
        if key in self.SeqList:
            ipos = self.SeqList.index(key)
            print("查找成功！值为",self.SeqList[ipos],"的元素，位于当前顺序表的第",ipos+1,"个位置")
        else:
            print("查找失败！当前顺序表中不存在值为",key,"的元素")

    def InsertElement(self):     #指定位置插入元素函数
        iPos = int(input("请输入待插入元素的位置："))
        Element = int(input("请输入待插入的元素值："))
        self.SeqList.insert(iPos,Element)
        print("插入元素后，当前顺序表为：\n",self.SeqList)

    def  DeleteElement(self):     #指定位置删除元素函数
        dPos = int(input("请输入待删除的元素的位置："))
        print("正在删除元素",self.SeqList[dPos],"...")
        self.SeqList.remove(self.SeqList[dPos])
        print("删除后顺序表为：\n",self.SeqList)

    def TravelElement(self):   #遍历顺序表元素函数
        SeqListLen = len(self.SeqList)
        print("******遍历列表中元素******")
        for i in range(0,SeqListLen):
            print("第",i+1,"个元素的值为",self.SeqList[i])

    def GetExtremum(self):      #求顺序表最值函数
        while True:
            print("********************************************")
            print("*1：查询最大值")
            print("*2：查询最小值")
            print("*3：查询最大值和最小值")
            print("*0：退出程序")
            print("********************************************")
            i = int(input("请输入："))
            if i == 1:
                print("顺序表中最大值为：",max(self.SeqList))
            elif i == 2:
                print("顺序表中最小值为：",min(self.SeqList))
            elif i == 3:
                print("顺序表中最大值为：",max(self.SeqList))
                print("顺序表中最小值为：", min(self.SeqList))
            elif i == 0:
                break
            else:
                print("输入不正确")