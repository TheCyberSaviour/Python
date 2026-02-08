#EnCode and DeCode

def EnCode():
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    print("Enter Value/String to EnCode...")
    decode = input()
    encode = ""
    for i in range(len(decode)):
        encode += alphabets[(alphabets.index(decode[i]) + 3) % 26]
    print(encode)


def DeCode():
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    print("Enter Value/String to DeCode...")
    encode = input()
    decode = ""
    for i in range(len(encode)):
        decode += alphabets[(alphabets.index(encode[i]) - 3) % 26]
    print(decode)


def main():
    print("Press 1 to EnCode...")
    print("Press 2 to DeCode...")
    print("Press 0 to Exit")
    choice = int(input())
    if choice == 1:
        EnCode()
    elif choice == 2:
        DeCode()
    else:
        exit(main)
main()