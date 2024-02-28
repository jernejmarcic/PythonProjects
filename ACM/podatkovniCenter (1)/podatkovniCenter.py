import csv

"""
Program has to:
 - Start with main door opening
 - If any of the doors are left opened after main door close == ERROR
 - If main door closes without error, then:
    * Write the number deignation of door that was opened at lest once to stdout 
"""





vhod = "vhod.txt"
doors_changes_str = []
doors_states = []
forgotenDoors = []
open_file = open(vhod)
file_parse = csv.DictReader(open_file)


for line in file_parse:
 print(line)
 doors_changes_str.extend(line['door'])
 doors_states.extend(line['state'])
 
 

doors_changes = list(map(int, doors_changes_str))

biggestDoor = max(doors_changes)
print(biggestDoor)
print(doors_changes)
# print(doors_changes)
if doors_changes[0] != doors_changes[len(doors_changes)-1]:
 print("You forgot to close the main door dummy")
 
else:
 print(doors_states)
 if doors_states.count('0') == doors_states.count('1'):
  doors_used_str = []
  for door in doors_changes:
   if door not in doors_used_str:
    doors_used_str.append(door)

  doors_used = list(map(int, doors_used_str))
  doors_used.sort()
# print(doors_used)
  print(f"{len(doors_used)} doors were used at least once, used doors: {doors_used}")

  
  
 else:
 
  print(f"You forgot to close a door")
 
