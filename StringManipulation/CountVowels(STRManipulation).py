#Count Vowels (STR Manipulation)
print("Enter a Sentence to count Vowels")
instring = input()


def iterativeVowels(instring):
    count = 0
    for x in range(len(instring)):
        mychar = instring[0]
        if mychar == "A" or mychar == "a" or mychar == "E" or mychar == "e" or mychar == "I" or mychar == "i" or mychar == "O" or mychar == "o" or mychar == "U" or mychar == "u":
            count = count + 1
        instring = instring[1:len(instring)]
    return count


result = iterativeVowels(instring)
print("Total Number of Vowels are,", result)
iterativeVowels(instring)