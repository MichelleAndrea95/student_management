import unittest
from unittest.mock import patch
import crud_operations 

class StudentManagementTest(unittest.TestCase):
    
    def setUp(self):
       
        crud_operations.students.clear()

    def test_add_student(self):
        
        crud_operations.add_student(7, "Michelle", 29, "VG", ["math", "sv"])
        
        
        self.assertEqual(len(crud_operations.students), 1)
        self.assertEqual(crud_operations.students[0].name, "Michelle")  

    @patch("builtins.print")  
    def test_view_students(self, mock_print):
        
        crud_operations.add_student(7, "Michelle", 29, "VG", ["math", "sv"])
        crud_operations.add_student(8, "Florence", 28, "VG", ["math", "sv"])

        crud_operations.view_students()

        
        mock_print.assert_any_call("ID: 7, Namn: Michelle, Ålder: 29, Betyg: VG, Ämnen: math, sv")
        mock_print.assert_any_call("ID: 8, Namn: Florence, Ålder: 28, Betyg: VG, Ämnen: math, sv")

    
    
from crud_operations import add_student, delete_student, update_name, update_age, update_grade, update_subjects
from student import Student

class StudentManagementTest(unittest.TestCase):
    def test_update_student_name(self):
        students = [Student(1, "John", 20, "A", ["Math", "Physics"])]
        result = update_name(students, 1, "Jonathan")
        self.assertTrue(result)  
        self.assertEqual(students[0].name, "Jonathan")

    def test_update_student_age(self):
        students = [Student(1, "John", 20, "A", ["Math", "Physics"])]
        result = update_age(students, 1, 21)
        self.assertTrue(result)
        self.assertEqual(students[0].age, 21)

    def test_update_student_grade(self):
        students = [Student(1, "John", 20, "A", ["Math", "Physics"])]
        result = update_grade(students, 1, "A+")
        self.assertTrue(result)
        self.assertEqual(students[0].grade, "A+")

    def test_update_student_subjects(self):
        students = [Student(1, "John", 20, "A", ["Math", "Physics"])]
        result = update_subjects(students, 1, ["Biology", "Chemistry"])
        self.assertTrue(result)
        self.assertEqual(students[0].subjects, ["Biology", "Chemistry"])

    def test_update_student_invalid_id(self):
        students = [Student(1, "John", 20, "A", ["Math", "Physics"])]
        result = update_name(students, 99, "NonExistent")
        self.assertFalse(result)  
    def test_delete_student(self):
        students = [
            Student(1, "John", 20, "A", ["Math", "Physics"]),
            Student(2, "Anna", 22, "B", ["Biology", "Chemistry"]),
        ]
        result = delete_student(students, 1)
        self.assertTrue(result)  
        self.assertEqual(len(students), 1)  
        self.assertEqual(students[0].id, 2)  

    def test_delete_student_invalid_id(self):
        students = [
            Student(1, "John", 20, "A", ["Math", "Physics"]),
            Student(2, "Anna", 22, "B", ["Biology", "Chemistry"]),
        ]
        result = delete_student(students, 99)
        self.assertFalse(result)  
        self.assertEqual(len(students), 2) 

if __name__ == "__main__":
    unittest.main()
