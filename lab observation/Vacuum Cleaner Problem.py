
rooms = {'A': 'Dirty', 'B': 'Dirty'}
position = 'A'

while 'Dirty' in rooms.values():
    print("Position:", position)
    if rooms[position] == 'Dirty':
        rooms[position] = 'Clean'
        print(position, "cleaned")
    else:
        position = 'B' if position == 'A' else 'A'

    if 'Dirty' in rooms.values() and rooms[position] == 'Clean':
        position = 'B' if position == 'A' else 'A'

print("All rooms cleaned:", rooms)
