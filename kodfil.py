# student_management.py

# Lista för att lagra studenter
students = []

# CRUD-funktioner
def add_student():
    # Logik för att lägga till student
    pass

def view_students():
    # Logik för att visa studenter
    pass

def update_student():
    # Logik för att uppdatera en student
    pass

def delete_student():
    # Logik för att ta bort en student
    pass

# Meny för att interagera med användaren
def main_menu():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Starta programmet
if __name__ == "__main__":
    main_menu()
