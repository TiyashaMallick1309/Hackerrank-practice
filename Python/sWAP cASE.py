def swap_case(s):
    str=""
    for i in s:
        if (i.isnumeric()):
            str+=i
        elif (i.islower()):
            str+=i.upper()
        elif(i.isupper()):
            str+=i.lower()
        else:
            str+=i
    return str
