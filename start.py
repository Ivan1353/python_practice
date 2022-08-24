import os
from pathlib import Path

myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(Path(r'C:\Users\Al', filename))

Path('spam') / 'bacon' / 'eggs'

os.chdir(r"C:\Users\ivand\PycharmProjects\automate\bam")
os.makedirs("spam.txt")

path = os.path.abspath(path)

path.anchor
path.name
path.stem
path.suffix
path.drive

calcFilePath = r"C:\Users\ivand\PycharmProjects\automate\calc.exe"
os.path.basename(calcFilePath)
os.path.dirname(calcFilePath)
calcFilePath.split(os.sep)

os.chdir(r"C:\Windows\System32")
os.path.getsize(".\calc.exe")

path = Path.cwd()

totalSize = 0
for filename in os.listdir(path):
    totalSize += os.path.getsize(os.path.join(path, filename))
print(totalSize)

os.path.isdir(dDrive)
#create txt

baconFile = open("bacon.txt", "w")
bacon_text = baconFile.read()
baconFile.write("I love bacon!")
