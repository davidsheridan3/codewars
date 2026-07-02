def lowercase_count(strng):
    count = 0
    for char in strng:
        if char.islower():
            count += 1
    return count