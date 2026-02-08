def Replace(original_chr, original_str, new_chr):
    #Variable to store the Resultant String
    new_str = ""
    for char in original_str:
        if char == original_chr:
            new_str = new_str + new_chr
        else:
            new_str = new_str + char
    return new_str


print("Enter String...")
original_str = input()
print("Enter Character you want to Replace...")
original_chr = input()
print("Enter New Character you want to Replace with...")
new_chr = input()
result = Replace(original_chr, original_str, new_chr)
print(result)