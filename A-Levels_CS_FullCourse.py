# AS and A2 Programming :3


myarray = [42, 27, 89, 23, 56, 78, 34, 92, 65, 12]


def choice():
    x = 0
    digit = 999
    while digit != 0:
        print("Enter 1 to Open Message")
        print("Enter 2 to Linear_Search in List")
        print("Enter 3 to Binary_Search in List")
        print("Enter 4 to Bubble_Sort in List")
        print("Enter 5 to Insertion_Sort in List")
        print("Enter 6 to Append Values in List")
        print("Enter 7 to Delete Value from List")
        print("Enter 8 to View the List")
        print("Enter 0 to EXIT Program")
        digit = int(input())
        print("----------------------------------------")
        if digit == 1:
            print("Welcome to my World")
            print("----------------------------------------")
        elif digit == 2:
            print("Please Sort your List in an Order before Searching...")
            print("Do you still want to continue?", "Enter y or n...")
            changes = str(input())
            if changes == "y":
                print("----------------------------------------")
                callable(linear_search())
        elif digit == 3:
            print("Please Sort your List in an Order before Searching...")
            print("Do you still want to continue?", "Enter y or n...")
            changes = str(input())
            if changes == "y":
                print("----------------------------------------")
                callable(binary_search())
        elif digit == 4:
            print("Bubble Sorting your array will permanently make changes...")
            print("Do you still want to continue?", "Enter y or n...")
            changes = str(input())
            if changes == "y":
                print("----------------------------------------")
                callable(bubble_sort())
        elif digit == 5:
            print("Insertion Sorting your array will permanently make changes...")
            print("Do you still want to continue?", "Enter y or n...")
            changes = str(input())
            if changes == "y":
                print("----------------------------------------")
                callable(insertion_sort())
        elif digit == 6:
            callable(append_element())
        elif digit == 7:
            callable(del_element())
        elif digit == 8:
            print(myarray)
            print("----------------------------------------")


def linear_search():
    print("Enter Number to Search")
    val = int(input())
    x = 0
    flag = False
    while x <= 9 and flag is False:
        if val == myarray[x]:
            print("Value Found in Array!")
            print("----------------------------------------")
            flag = True
        x = x + 1
    if flag is False:
        print("Value NOT Found in Array...")
        print("----------------------------------------")


def bubble_sort():
    print("Unsorted Array :-")
    print(myarray)
    swap = True
    temp = 0
    while swap is True:
        swap = False
        for x in range(0, 9):
            if myarray[x] > myarray[x + 1]:
                temp = myarray[x]
                myarray[x] = myarray[x + 1]
                myarray[x + 1] = temp
                swap = True
    print("Sorted Array :-")
    print(myarray)
    print("----------------------------------------")


def binary_search():
    found = False
    lower = 0
    upper = 9
    middle = 0
    valtosearch = 0
    print("Enter Integer Value to Search in List...")
    valtosearch = int(input())
    while upper >= lower and found is False:
        middle = upper + lower // 2
        if myarray[middle] == valtosearch:
            found = True
        elif valtosearch > myarray[middle]:
            lower = middle + 1
        elif valtosearch < myarray[middle]:
            upper = middle - 1

    if found is True:
        print("Value Found in List!")
        print("----------------------------------------")
    elif found is False:
        print("Value NOT Found in List")
        print("----------------------------------------")


def insertion_sort():
    for x in range(len(myarray)):
        i = x
        temp = myarray[x]
        while i > 0 and myarray[i - 1] > temp:
            myarray[i] = myarray[i - 1]
            i -= 1
            myarray[i] = temp
    print(myarray)
    print("----------------------------------------")


def append_element():

    num = -1
    while num != 0:
        print("Enter 1 to Populate List")
        print("Enter 2 to View List")
        print("Enter 0 to Stop")

        num = int(input())
        if num == 1 or 2:
            if num == 1:
                print("Enter Integer Value : ")
                instring = int(input())
                myarray.append(instring)
            elif num == 2:
                print("----------------------------------------")
                print("Updated List : ", myarray)
                print("----------------------------------------")
        else:
            print("Wrong Choice Made :( ")


def del_element():
    print("Enter Value to Delete from List")
    delVal = int(input())
    for x in range(len(myarray)):
        if myarray[x] == delVal:
            myarray.pop(x)


choice()