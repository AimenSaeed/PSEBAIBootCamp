"""
Name : Aimen Saeed
Trainee ID : TRN-2026-000352
Date : 10-11-26
"""
# Warm up: Shopping list
items=["milk", "bread", "eggs"]
items.append("butter")
items.remove("bread")
items.sort()
for enum, item in enumerate(items):
    print(f"{enum+1}. {item}")

# Build: Phone book
contacts ={
    "Aimen": "123-456-7890",
    "Tooba": "987-654-3210",
    "Kaneeza": "555-555-5555",
    "Amna": "111-222-3333",
    "Gull": "444-444-4444"
}
print("""
======= Phone Book =======
1. Add Contact
2. Search Contact
3. Delete Contact
4. Show all Contacts
5. Exit
===========================
""")
while True:
    choice = input("Enter your choice (1-5): ")
    if choice == "1":
        name = input("Enter contact name: ")
        number = input("Enter contact number: ")
        contacts[name] = number
        print(f"Contact {name} added.")
    elif choice == "2":
        name = input("Enter contact name to search: ")
        if name in contacts:
            print(f"{name}: {contacts[name]}")
        else:
            print(f"Contact {name} not found.")
    elif choice == "3":
        name = input("Enter contact name to delete: ")
        if name in contacts:
            del contacts[name]
            print(f"Contact {name} deleted.")
        else:
            print(f"Contact {name} not found.")
    elif choice == "4":
        print("All Contacts:")
        for name, number in contacts.items():
            print(f"{name}: {number}")
    elif choice == "5":
        print("Exiting phone book.")
        break
    else:
        print("Invalid choice. Please try again.")

# Challenge: Class result sheet
marks = {
    "Ali" : [80,72,91],
    "Sara" :[95,88,90],
    "Iqra" : [70,75,80,85],
    "Zainab" : [88,39,85],
    "Saeed" : [60,65,70]
}
total_marks={}
for student, scores in marks.items():
    total=sum(scores)
    total_marks[student]=total
    average=total/len(scores)  
    print(f"{student}: Total Marks = {total}, Average Marks = {average:.2f}")
    for score in scores:
        if score < 40:
            print(f"{student} has scored less than 40 in one or more subjects.")
max_student=max(total_marks, key=total_marks.get)
print(f"Class Topper: {max_student} with {total_marks[max_student]} marks.")
