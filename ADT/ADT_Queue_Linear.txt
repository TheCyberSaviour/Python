def Enqueue():
    global QueueData
    global QueueHead
    global QueueTail
    InsertData = ""
    if QueueTail == 19 or QueueTail > 19:
        return False
    if QueueTail == -1:
        QueueHead = 0
    print("Enter Data to Enqueue")
    InsertData = input()
    QueueTail = QueueTail + 1
    QueueData[QueueTail] = InsertData
    return True


def Dequeue():
    global QueueData
    global QueueHead
    global QueueTail
    if QueueHead < 0 or QueueHead > 3 or QueueHead > QueueTail:
        return False
    else:
        QueueHead = QueueHead + 1
        return QueueHead[QueueHead - 1]


QueueData = []
QueueHead = -1
QueueTail = -1
for i in range(0, 3):
    QueueData.append("")

num = -1
choice = ""
while choice != "n":
    print("Enter 1 to Enqueue")
    print("Enter 2 to Dequeue")
    print("Enter 3 to print QueueData(List)")
    num = int(input())
    if num == 1 and choice != "n":
        Enqueue()
    elif num == 2 and choice != "n":
        result_dequeue = Dequeue()
        print(result_dequeue)

    elif num == 3 and choice != "n":
        for x in range(0, 3):
            print(QueueData[x])
    else:
        print("Wrong Choice! Please Input Integer and Correct Value from the Menu")

    print("Do you want to continue? Enter 'no' to Stop")
    choice = input()