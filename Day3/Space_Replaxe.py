def remove_extra_spaces(string):
    res = ""
    prev = ""
    for c in string:
        if not (c == " " and prev == " "):
            res += c
        prev = c
    return res

string = input("Enter the string:")
print(remove_extra_spaces(string))
