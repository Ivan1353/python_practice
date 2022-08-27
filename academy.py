number = int(input())
students = dict()
counter = 0

for i in range(0, 2*number):
    info = input()
    if counter%2 == 0:
        name = info
        counter +=1
        continue
    else:
        grade = float(info)
        counter += 1
    if name not in students:
        students[name] = [grade]
    else:
        students[name].append(grade)

for student in students:
    average_grade = sum(students[student])/len(students[student])
    if average_grade >= 4.5:
        print(f"{student} -> {average_grade:.2f}")