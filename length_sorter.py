def length_sorter(list1):
    dict1 = {}
    for word in list1:
        if len(word) not in dict1:
            dict1[len(word)] = [word]
        else:
            dict1[len(word)].append(word)
    return dict1
