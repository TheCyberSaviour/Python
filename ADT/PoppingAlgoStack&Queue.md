# Stack + UDT
## Pop():

* if TopPointer = 0 then Error StackEmpty
* print Stack[TopPointer].Name #Value Popped
* TempPointer = TopPointer
* TopPointer = Stack[TempPointer].Pointer
* Stack[TempPointer].Pointer = FreePointer
* FreePointer = TempPointer

# Queue + UDT
## Pop():

* if HeadPointer = 0 then Error QueueEmpty
* print Queue[HeadPointer].Name #Value Dequeued
* TempPointer = HeadPointer
* HeadPointer = Queue[TempPointer].Pointer
* if HeadPointer = 0 then TailPointer = 0
* Queue[TempPointer].Pointer = FreePointer
* FreePointer = CurrentPointer