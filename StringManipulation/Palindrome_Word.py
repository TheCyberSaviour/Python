def IsPalindrome():

    print("Enter Word to Check Palindrome")
    word = (input())
    check = ""

    for alphabet in word:
        check = alphabet + check
    if word == check:
        print("Palindrome!")
    else:
        print("Not Palindrome")

IsPalindrome()