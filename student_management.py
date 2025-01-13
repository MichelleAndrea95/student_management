import json

students= []

class Student:
    def __init__(self, student_id, name, age, grade, subjects):
        self.id = student_id
        self.name = name
        self.age = age
        self.grade = grade
        self.subjects = subjects

    def update_info(self, attribute, new_value):
        if hasattr(self, attribute):
            setattr(self, attribute, new_value)
        else:
            raise AttributeError(f"{attribute} is not a valid attribute.")

    def __str__(self):
        return (f"ID: {self.id}, Name: {self.name}, Age: {self.age}, "
                f"Grade: {self.grade}, Subjects: {', '.join(self.subjects)}")









