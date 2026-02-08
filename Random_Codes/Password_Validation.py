# A simple program for Password Validation Check

def main():
    print("Enter Valid Password...")
    print("Password Should be 8-30 Characters.")
    print("'TIP: Use of Numbers and Special Characters makes your Password Strong'")
    passwd = input()
    check_password(passwd)


def check_password(passwd):
    number = ""
    text = ""
    sp_char = ""
    up_char = False
    sp_chars = "!@#$%^&*()_+=~`:;"'<,>.?/'

    if passwd != "" and 8 <= len(passwd) <= 30:
        for char in passwd:
            if char.isupper():
                up_char = True
            elif char.isdigit():
                number = number + char
            elif char in sp_chars:
                sp_char = sp_char + char
            else:
                text = text + char
    else:
        main()
    if number != "" and len(number) >= 2 and sp_char != "" and up_char is True:
        print("Very Strong Password")
    elif number != "" and sp_char != "":
        print("Strong Password")
    elif number != "" and sp_char == "":
        print("Strong Password")
    elif number == "" and sp_char != "":
        print("Strong Password")
    else:
        print("Weak Password")

main()