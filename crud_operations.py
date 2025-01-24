
import json
from student import Student
students=[]


def add_student(id, name, age, grade, subjects):
    new_student = Student(id, name, age, grade, subjects)
    students.append(new_student)


def view_students():
    print(students)
    if not students:  
        print("Det finns inga studenter i systemet.")
        return
    
    print("\nLista på alla studenter:")
    for student in students:
        print(f"ID: {student.id}, Namn: {student.name}, Ålder: {student.age}, Betyg: {student.grade}, Ämnen: {', '.join(student.subjects)}")
    print()
    

def update_name(students, id, new_name):
    for student in students:
        if student.id == id:
            student.name = new_name
            return True  
    return False  


def update_age(students, id, new_age):
    for student in students:
        if student.id == id:
            student.age = new_age
            return True
    return False


def update_grade(students, id, new_grade):
    for student in students:
        if student.id == id:
            student.grade = new_grade
            return True
    return False


def update_subjects(students, id, new_subjects):
    for student in students:
        if student.id == id:
            student.subjects = new_subjects
            return True
    return False

def delete_student(students, id):
    for i, student in enumerate(students):
        if student.id == id:
            del students[i]
            return True  
    return False  

def load_students_from_file(file="students.json"):
    """Läser in studentdata från en JSON-fil."""
    students = []
    try:
        with open(file, "r") as f:  
            data= json.load(f)  
            students = [Student.from_dict(student) for student in data]
    except (FileNotFoundError, json.JSONDecodeError):
        print(f"Filen {file} kunde inte läsas. Skapar en tom lista.")
    


def save_and_quit(file_path="students.json"):
    try:
      
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump([student.to_dict() for student in students], f, indent=4)
        print("Data har sparats till fil.")
    except Exception as e:
        print(f"Ett fel uppstod vid sparandet: {e}")
    
    print(f"Studentdata har sparats i dokumentet '{file_path}'.")
    return

 
