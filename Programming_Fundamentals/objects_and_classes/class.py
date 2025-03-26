class Class:
    __students_count = 22

    def __init__(self, name: str):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name: str, grade: float):
        if len(self.students) < Class.__students_count:
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        if self.grades:
            average = sum(self.grades) / len(self.grades)
            return round(average, 2)
        return 0

    def __repr__(self):
        students_str = ", ".join(self.students)
        average_grade = self.get_average_grade()
        return f"The students in {self.name}: {students_str}. Average grade: {average_grade}"
    
    def __str__(self):
        return self.__repr__()

a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)
