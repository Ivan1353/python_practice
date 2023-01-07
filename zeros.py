def move_zeros(lst):
    zero_count= 0
    for element in lst:
        if element == 0:
            lst.remove(element)
            zero_count += 1
    new_list = lst
    print(lst)
    for i in range (zero_count):
        new_list.append(0)

    return new_list