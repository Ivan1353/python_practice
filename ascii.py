info = input().split(', ')
dict1 = dict()
for letter in info:
    dict1[letter] = ord(letter)
print(dict1)