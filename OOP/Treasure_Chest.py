class TreasureChest:
    #Private Question : String
    #Private Answer : Integer
    #Private Points : Integer

    def __init__(self, question, answer, points):
        self.__question = question
        self.__answer = answer
        self.__points  = points

    def getQuestion(self):
        return self.__question

    def checkAnswer(self, ans):
        if int(self.__answer) ==  ans:
            return True
        else:
            return False

    def getPoints(self, attempts):
        if attempts == 1:
            return self.__points
        elif attempts == 2:
            return self.__points // 2
        elif attempts == 3:
            return self.__points // 4
        else:
            return 0

arrayTreasure = []

def readData():
    global arrayTreasure

    try:
        FileHandle = open("TreasureChestData.txt", "r")
        line = FileHandle.readline().strip()
        int_line = 1
        while line != "" and int_line < 16:
            question = line
            lint_ine= int_line + 1
            answer = FileHandle.readline().strip()
            lint_ine = int_line + 1
            points = FileHandle.readline().strip()
            lint_ine = int_line + 1
            arrayTreasure.append(TreasureChest(question, answer, points))
            line = FileHandle.readline().strip()
        FileHandle.close()
    except IOError:
        print("File Not Found")

readData()

num = int(input("Select Treasure Chest (1-5)"))
if 0 < num < 6:
    flag = False
    attempt = 0
    while (flag == False and attempt < 4):
        ans = int(input(f"{arrayTreasure[num - 1].getQuestion()} : "))
        flag = arrayTreasure[num - 1].checkAnswer(ans)
        attempt = attempt + 1
    print(int(arrayTreasure[num-1].getPoints(attempt)))