# Meny för att interagera med användaren
from crud_operations import add_student, delete_student, update_student, view_students

    
def main_menu():
    while True:
        choice = input("välj ett alternativ: ")

        print("\nStudent Management System")
        print("1. Lägg till student")
        print("2. Lista på alla studenter")
        print("3. Uppdatera lista på studenter")
        print("4. Radera Student")
        print("5. Exit")

      

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Avslutar programmet.")
            break
        else:
            print("Fel inmatning. Välj ett nytt val.")
        
# Starta programmet
if __name__ == "__main__":
    main_menu()
