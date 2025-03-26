pairs = int(input())
students = {}

for _ in range(pairs):
    student_name = input()
    student_grade = float(input())

    if student_name not in students:
        students[student_name] = []
    students[student_name].append(student_grade)

filtered_students = {}

for student, grades in students.items():
    average = sum(grades) / len(grades)

    if average >= 4.50:
        filtered_students[student] = average


for student, grade in sorted(filtered_students.items(), key=lambda x: (list(students.keys()).index(x[0]))):
    print(f"{student} -> {grade:.2f}")
