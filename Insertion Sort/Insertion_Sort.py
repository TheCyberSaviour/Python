def i_s():
    mylist = [3, 27, 89, 23, 56, 78, 34, 92, 65, 12]
    print(mylist)
    for x in range(0, 10):
        i = x
        temp = mylist[x]
        while i > 0 and mylist[i - 1] > temp:
            mylist[i] = mylist[i - 1]
            i -= 1
            mylist[i] = temp
    print(mylist)


i_s()