
from school.student import Student, get_grade, make_comment
from school.manager import SchoolManager


def show_menu() -> None:
    print("\n===== SCHOOL MANAGER =====")
    print("1. Add student")
    print("2. Add marks")
    print("3. Show report card")
    print("4. Class ranking")
    print("5. Write comment")
    print("6. Save and exit")


def main() -> None:
    manager = SchoolManager()
    manager.load()

    while True:
        show_menu()

        try:
            choice = input("Choose: ")

            if choice == "1":
                name = input("Student name: ")
                roll = int(input("Roll number: "))

                manager.add_student(Student(name, roll))
                print("Student added!")

            elif choice == "2":
                roll = int(input("Roll number: "))
                marks = list(map(int, input("Enter marks separated by spaces: ").split()))

                manager.add_marks(roll, marks)
                print("Marks added!")

            elif choice == "3":
                roll = int(input("Roll number: "))
                student = manager.find_student(roll)

                avg = student.average()

                print("Name:", student.name)
                print("Roll:", student.roll_no)
                print("Marks:", student.marks)
                print("Average:", avg)
                print("Grade:", get_grade(avg))

            elif choice == "4":
                for student in manager.ranking():
                    print(student.name, student.average())

            elif choice == "5":
                roll = int(input("Roll number: "))
                student = manager.find_student(roll)
                print(make_comment(student))

            elif choice == "6":
                manager.save()
                print("Data saved. Goodbye!")
                break

            else:
                print("Invalid menu choice")

        except (ValueError, TypeError) as error:
            print("Error:", error)

        except Exception:
            print("An unexpected error occurred.")
if __name__ == "__main__":
    main()
if __name__ == "__main__":
    main()
