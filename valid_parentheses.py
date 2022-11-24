def valid_parentheses(string):
    parentheses = "".join([x for x in string if x == "(" or x == ")"])
    while True:
        if parentheses != parentheses.replace("()", ""):
            parentheses = parentheses.replace("()", "")
        else:
            break
    if parentheses:
        return False
    else:
        return True
