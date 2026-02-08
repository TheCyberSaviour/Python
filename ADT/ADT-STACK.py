#ADT (Abstract Data Type) STACK

def stack():
    mystack = []
    num = 999
    tp = 0

    while num != 0:
        print("----------------------------------")
        print("Enter 1 to PUSH in Stack")
        print("Enter 2 to POP in Stack")
        print("Enter 3 to Traverse Stack")
        print("Enter 0 to EXIT")
        num = int(input())

        if num == 1:
            callable(push_stack(mystack, tp))
        elif num == 2:
            callable(pop_stack(mystack, tp))
        elif num == 3:
            callable(traverse_stack(mystack))
        elif num == 0:
            break
        else:
            print("Please Choose Correct...")

def push_stack(mystack, tp):
    if tp > len(mystack):
        print("Error!, Overflow...")
    else:
        print("Enter Value to Push in Stack")
        val = input()
        mystack.append(val)
        tp = tp + 1
    return tp


def pop_stack(mystack, tp):
    if tp < 0:
        print("Error!, Underflow...")
    else:
        tp = tp - 1
        print("Popped Value :", mystack[tp])
    return tp

def traverse_stack(mystack):
    if len(mystack) == 0:
        print("Stack Empty")
    else:
        for x in range(0, len(mystack)):
            print(mystack[x])

stack()