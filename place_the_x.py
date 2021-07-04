row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")


first = int(position[0])
second = int(position[1])

firstnum = first - 1
secnum = second - 1

xspot = map[secnum][firstnum] = "X"

new = (f"{row1}\n{row2}\n{row3}")

print(new)