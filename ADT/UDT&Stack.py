#UDT + Stack 
class Node:   #UDT
    def __init__(self, name : str, pointer : int):
        self.name = name
        self.pointer = pointer

Stack = [Node("", 1) for _ in range(10)]   #ArrayDeclared with UDT

TopOfStackPointer = 0   #Latest Value Inserted
FreePointer = 0   #Point the Next Available Space in Array
TempPointer = 0   #Variable to Copy FreePointer


def Push(NewName:str):   #Parameter as Value to Insert
    global Stack   #Array as Node
    global TopOfStackPointer
    global FreePointer
    global TempPointer

    if FreePointer == -1:
        return -1
    else:
        #Insert Value in Array
        Stack[FreePointer].name = NewName
        
        #Copy FreePointer to a Variable
        TempPointer = FreePointer
        
        #Next Available Space in FreePointer
        FreePointer = Stack[FreePointer].pointer
        
        #For Pop Operations
        Stack[TempPointer].pointer = TopOfStackPointer
        
        #Where was the Value Added Recently
        TopOfStackPointer = TempPointer


Push("Dog")
Push("Cat")
for node in Stack:
    print(f"Name: {node.name} Pointer: {node.pointer}")