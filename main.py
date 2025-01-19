# Meny för att interagera med användaren
from crud_operations import add_student,update_name,update_age, update_grade,update_subjects,view_students,delete_student,load_students_from_file,save_and_quit
   

def main_menu():
    file_path = "students.json"
    students = load_students_from_file(file_path)  # Läs in studenter vid start
    students=[]
    while True:
        print("\nStudent Management System")
        print("1. Lägg till student")
        print("2. Lista på alla studenter")
        print("3. Uppdatera lista på studenter")
        print("4. Radera Student")
        print("5. Stäng ner och spara data")
        choice = input("välj ett alternativ: ")

        if (choice == "1"):
            id = int(input("Välj ett id för student\n"))
            name = input("Välj ett namn för student\n")
            age = int(input("Välj en ålder för student\n"))
            grade = input("Välj ett betyg för student\n")
            subjects = input("Välj kommaseparerade ämnen för student\n")
            subjects = subjects.split(",")
            add_student(id, name, age, grade, subjects)

        elif (choice == "2"):
            view_students()
        
        elif (choice == "3"):
                
                print("\nStudent Management System")
                print("1. Visa alla studenter")
                print("2. Uppdatera namn på student")
                print("3. Uppdatera ålder på student")
                print("4. Uppdatera betyg på student")
                print("5. Uppdatera ämnen på student")
                print("6. Avsluta")
                choice = input("Välj ett alternativ (1-6): ")

                if choice == '1':
            # Visa alla studenter
                        for student in students:
                         print(f"{student.id}: {student.name}, {student.age} år, {student.grade}, Ämnen: {', '.join(student.subjects)}")
            # Visa alla studenter 
                elif choice == '2':
            # Uppdatera studentens namn
                    student_id = int(input("Ange studentens ID: "))
                    new_name = input("Ange det nya namnet: ")
                    update_name(student_id, new_name)
                elif choice == '3':
            # Uppdatera studentens ålder
                    student_id = int(input("Ange studentens ID: "))
                    new_age = int(input("Ange den nya åldern: "))
                    update_age(student_id, new_age)
        
                elif choice == '4':
            # Uppdatera studentens betyg
                    student_id = int(input("Ange studentens ID: "))
                    new_grade = input("Ange det nya betyget: ")
                    update_grade(student_id, new_grade)
        
                elif choice == '5':
            # Uppdatera studentens ämnen
                    student_id = int(input("Ange studentens ID: "))
                    new_subjects = input("Ange de nya ämnena, separerade med kommatecken: ").split(",")
                    update_subjects(student_id, new_subjects)
        
                elif choice == '6':
            # Avsluta programmet
                    print("Avslutar programmet.")
                    break
        
                else:
                    print("Ogiltigt val. Försök igen.")

        elif (choice == "4"):
                
                students= delete_student(students)
                    
                
                del_student = int(input("Ange ID för den student du vill ta bort: "))

                students = [s for s in students if s["id"] != del_student]

                print(f"ID {id} är raderad")
        elif choice == "5":
            save_and_quit(students, file_path="students.json")
            break
        else:
            print("Ogiltigt val.")
    
if __name__ == "__main__":
    main_menu()
