import unittest
from student_management import Student

class TestStudentManagement(unittest.TestCase):
    def setUp(self):
        self.student = Student(1, "Test Student", 20, "VG", ["Math", "Science"])

    def test_student_creation(self):
        self.assertEqual(self.student.id, 1)
        self.assertEqual(self.student.name, "Test Student")
        self.assertEqual(self.student.age, 20)
        self.assertEqual(self.student.grade, "VG")
        self.assertEqual(self.student.subjects, ["Math", "Science"])

    def test_update_info(self):
        self.student.update_info("name", "Updated Name")
        self.assertEqual(self.student.name, "Updated Name")

    def test_invalid_update(self):
        with self.assertRaises(AttributeError):
            self.student.update_info("invalid_attribute", "value")

    def test_to_dict_and_from_dict(self):
        student_dict = self.student.to_dict()
        self.assertEqual(student_dict["name"], "Test Student")
        recreated_student = Student.from_dict(student_dict)
        self.assertEqual(recreated_student.name, "Test Student")

if __name__ == "__main__":
    unittest.main()

