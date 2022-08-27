charList = list(input())
charDict = dict()
for char in charList:
    if char == ' ':
        charList.remove(char)

for char in charList:
    if char not in charDict:
        charDict[char] = 1
    else:
        charDict[char] += 1
for letter in charDict:
    print(f"{letter} -> {charDict[letter]}")