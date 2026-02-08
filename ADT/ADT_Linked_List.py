#Declare ArrayNodes : Integer
#Declare RootPointer : Integer
#Declare FreePointer : Integer

ArrayNodes = [[0 for X in range(3)] for Y in range(20)]
RootNode = -1
FreeNode = 0

def AddNode(ArrayNode, RootNode, FreeNode):
    #Declare placed : Boolean
    #Declare CurrentNode : Integer
    CurrentNode = 0
    placed = False

    NodeData = int(input("Enter New Data : "))

    if FreeNode <= 19:
        ArrayNodes[FreeNode][0] = -1
        ArrayNodes[FreeNode][1] = NodeData
        ArrayNodes[FreeNode][2] = -1
        if RootNode == -1:
            RootNode = 0
        else:
            placed = False
            CurrentNode = RootNode
            while placed == False:
                if NodeData < ArrayNodes[CurrentNode][1]:
                    if ArrayNodes[CurrentNode][0] == -1:
                        ArrayNodes[CurrentNode][0] = FreeNode
                        placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][0]
                elif ArrayNodes[CurrentNode][2] == -1:
                    ArrayNodes[CurrentNode][2] = FreeNode
                    placed = True
                else:
                    CurrentNode = ArrayNodes[CurrentNode][2]
        FreeNode = FreeNode + 1
    else:
        print("Tree is Full")
    return ArrayNodes, RootNode, FreeNode

def InOrder(ArrayNodes, RootNode):
    if ArrayNodes[RootNode][0] != -1:
        InOrder(ArrayNodes, ArrayNodes[RootNode][0])
    print(str(ArrayNodes[RootNode][1]))
    if ArrayNodes[RootNode][2] != -1:
        InOrder(ArrayNodes, ArrayNodes[RootNode[2]])


def PrintAll():
    global ArrayNodes
    print("LeftPointer", "", "Data", "", "RightPointer")
    for x in range(0, len(ArrayNodes)):
        print("  ", str(ArrayNodes[x][0]), "       ", str(ArrayNodes[x][1]), "      ", str(ArrayNodes[x][2]))


for x in range(0, 10):
    # AddNode(ArrayNodes, 0, x)
    ArrayNodes, RootPointer, FreeNode = AddNode(ArrayNodes, RootNode, FreeNode)
InOrder(ArrayNodes, RootNode)
PrintAll()