info = input().split(" ")
lowerList = []
for duma in info:
    lowerList.append(duma.lower())
dict1 = dict()
for word in lowerList:
    if word not in dict1:
        dict1[word] = 0
    if word in dict1:
        dict1[word] += 1
listOdd = [kluch for kluch in dict1 if dict1[kluch]%2 != 0]
print(" ".join(listOdd))