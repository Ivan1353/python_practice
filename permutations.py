import itertools

def permutations(s):
    elements = list(s)
    permlist = list(itertools.permutations(elements))
    list1 = ["".join(x) for x in permlist]
    return sorted(list(set(list1)))