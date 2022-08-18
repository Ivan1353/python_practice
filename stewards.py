from collections import deque

seats = input().split(", ")
seats_updated = []
seats_matched = []
endseats = []
rotations = 0

for seat in seats:
    seat_number = ""
    seat_letter = ""
    for ch in seat:
        if ch.isnumeric():
            seat_number += ch
        else:
            seat_letter = ch
    seats_updated.append((seat_number, seat_letter))


passengers1 = deque([int(x) for x in input().split(", ")])
passengers2 = deque([int(x) for x in input().split(", ")])

passenger = passengers1[0] + passengers2[-1]


while True:
    match = False
    if len(seats_matched) >= 3 or rotations >= 10:
        break

    passenger = passengers1[0] + passengers2[-1]
    letter = chr(passenger)

    for seat in seats_updated:
        if letter == seat[1]:
            if int(seat[0]) == passengers1[0] or int(seat[0]) ==  passengers2[-1]:
                seats_updated.remove(seat)
                seats_matched.append(seat)
                del passengers1[0], passengers2[-1]
                match = True

    if match == False:
        passengers1.append(passengers1.popleft())
        passengers2.appendleft(passengers2.pop())

    rotations += 1

seats_string = ''
for seat_tuple in seats_matched:
    seat = ''.join(seat_tuple)
    endseats.append(seat)
print(f"Seat matches: {', '.join(endseats)}")
print(f"Rotations count: {rotations}")