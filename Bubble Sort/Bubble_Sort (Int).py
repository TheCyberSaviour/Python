def b_sort():
    myarray = [10, 0, 29, 7, 1, 12, 20, 15, 27, 8]
    print("Unsorted Bubble Sort :", myarray)
    swap = True
    while swap is True:
        swap = False
        for x in range(0, 9):
            if myarray[x] > myarray[x + 1]:
                temp = myarray[x]
                myarray[x] = myarray[x + 1]
                myarray[x + 1] = temp
                swap = True
    print("Sorted Bubble Sort :", myarray)


b_sort()