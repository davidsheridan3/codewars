def same_case(a, b):
    if a.isalpha() == False or b.isalpha() == False:
        return -1
    elif a.isupper() == b.isupper():
        return 1
    elif a.isalpha() == True and b.isalpha() == True and a.isupper() != b.isupper():
        return 0