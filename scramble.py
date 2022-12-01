def scramble(s1, s2):
    list1, list2 = list(s1), list(s2)
    for letter in list1:
        if letter in list2:
            list2.remove(letter)
    if list2:
        return False
    else:
        return True