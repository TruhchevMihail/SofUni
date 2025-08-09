from unittest import TestCase, main

from project.student import Student


class StudentTests(TestCase):
    def setUp(self):
        self.student = Student("John")
        self.student_with_courses = Student("Jane", {"Math": ["test notes"]})

    def test_init_with_default_courses(self):
        self.assertEqual(self.student.name, "John")
        self.assertEqual(self.student.courses, {})

    def test_init_with_courses(self):
        self.assertEqual(self.student_with_courses.name, "Jane")
        self.assertEqual(self.student_with_courses.courses, {"Math": ["test notes"]})

    def test_enroll_existing_course(self):
        self.student_with_courses.enroll("Math", ["new note"])
        self.assertEqual(self.student_with_courses.courses, {"Math": ["test notes", "new note"]})
        result = self.student_with_courses.enroll("Math", ["another note"])
        self.assertEqual(result, "Course already added. Notes have been updated.")
        self.assertEqual(self.student_with_courses.courses, {"Math": ["test notes", "new note", "another note"]})

    def test_enroll_new_course_with_notes_default_param(self):
        result = self.student.enroll("Physics", ["note1", "note2"])
        self.assertEqual(result, "Course and course notes have been added.")
        self.assertEqual(self.student.courses, {"Physics": ["note1", "note2"]})

    def test_enroll_new_course_with_notes_Y_param(self):
        result = self.student.enroll("Chemistry", ["note1", "note2"], "Y")
        self.assertEqual(result, "Course and course notes have been added.")
        self.assertEqual(self.student.courses, {"Chemistry": ["note1", "note2"]})

    def test_enroll_new_course_without_notes(self):
        result = self.student.enroll("Biology", ["note1", "note2"], "N")
        self.assertEqual(result, "Course has been added.")
        self.assertEqual(self.student.courses, {"Biology": []})

    def test_add_notes_existing_course(self):
        result = self.student_with_courses.add_notes("Math", "new note")
        self.assertEqual(result, "Notes have been updated")
        self.assertEqual(self.student_with_courses.courses, {"Math": ["test notes", "new note"]})

    def test_add_notes_non_existing_course(self):
        with self.assertRaises(Exception) as context:
            self.student.add_notes("History", "new note")
        self.assertEqual(str(context.exception), "Cannot add notes. Course not found.")

    def test_leave_existing_course(self):
        result = self.student_with_courses.leave_course("Math")
        self.assertEqual(result, "Course has been removed")
        self.assertEqual(self.student_with_courses.courses, {})

    def test_leave_non_existing_course(self):
        with self.assertRaises(Exception) as context:
            self.student.leave_course("Art")
        self.assertEqual(str(context.exception), "Cannot remove course. Course not found.")

if __name__ == "__main__":
    main()
