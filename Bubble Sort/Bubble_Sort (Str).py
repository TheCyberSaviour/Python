students = ["H", "A", "Q", "F", "E", "U", "Z", "T", "S", "M", "D", "I", "O", "L", "W", "Y", "G", "X", "N", "C", "R", "P", "J", "K", "B", "V"]


def b_sort():
    swap = True
    while swap is True:
        swap = False
        for _ in range(0, 25):
            if students[_ + 1] < students[_]:
                temp = students[_ + 1]
                students[_ + 1] = students[_]
                students[_] = temp
                swap = True


def printarray():
    for _ in range(0, 26):
        if _ > 0:
            print("|", end='')
        print(students[_], end='')


b_sort()
printarray()