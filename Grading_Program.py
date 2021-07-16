student_score = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for item in student_score:
    if student_score[item] >= 91:
        student_grades[item] = "Outstanding"
    elif student_score[item] >= 81:
        student_grades[item] = "Exceeds Expectations"
    elif student_score[item] >= 71:
        student_grades[item] = "Acceptable"
    else:
        student_grades[item] = "Fail"



print(student_grades)