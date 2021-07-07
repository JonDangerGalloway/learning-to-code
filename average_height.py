student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

#180  124  165  173  189  169  146

total = 0
for height in student_heights:
  total = total + height

students = 0
for student in student_heights:
  students += 1

average = round(total / students)

print(average)