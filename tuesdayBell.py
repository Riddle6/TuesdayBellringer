# Collect the names of students and their grades, then loop through a dictionary to print out the list of Name : Grade.

grades = {"Connor": 73, "Gavin": 11, "Eva": 96, "Hannah": 85}

for key, value in grades.items():
    print(f"\nStudent: {key} \nGrade: {value}")