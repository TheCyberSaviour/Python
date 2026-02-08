def ReadWords(FileName):
    global WordArray
    global NumberWords
    r_file = open(FileName, "r")
    data = r_file.read().strip()
    r_file.close()
    WordArray = data.split()
    NumberWords = len(WordArray)
    Play()


def Play():
    global WordArray
    global NumberWords
    correct_answers = 0
    percentage = 0
    found = False
    answer = ""

    print("Main Word is :", WordArray[0])
    print("Number of Answers with 3 or more letters :", NumberWords - 1)
    WordArray[0] = ""

    while answer != "no":
        print("Enter your Word or 'no' to Stop")
        answer = input().lower()
        found = False

        if answer != "no":
            for x in range(0, NumberWords):
                if answer == WordArray[x]:
                    WordArray[x] = ""
                    correct_answers = correct_answers + 1
                    found = True
                    print("Correct! you have found", correct_answers, "answers")
            if found == False:
                print("Incorrect Word")

    percentage = int((correct_answers / (NumberWords - 1)) * 100)
    print("You Found", percentage, "% Correct Answers")
    if percentage < 100:
        print("The Words you Missed are :-")
        for x in range(0, NumberWords - 1):
            if WordArray[x] != "":
                print(WordArray[x])

WordArray = []
NumberWord = len(WordArray)
print("Enter 'easy', 'medium' or 'hard' to Play")
difficulty = input().lower()
if difficulty == "easy":
    ReadWords("C:/Users/mhass/Documents/Easy.txt")
elif difficulty == "medium":
    ReadWords("C:/Users/mhass/Documents/Medium.txt")
else:
    ReadWords("C:/Users/mhass/Documents/Hard.txt")