"""
Name : Aimen Saeed
Trainee ID : TRN-2026-000352
Date : 10-11-26
"""
# Warm-up: Safe Division:
try:
    num1=int(input("Enter 1st number: "))
    num2=int(input("Enter 2nd number: "))
    print(f"Quotient: {num1/num2}")
except ValueError:
    print("Invalid input. Please enter a number to divide")
except ZeroDivisionError:
    print("Cannot divide by zero. Please enter a non-zero number")

# Build: Daily Diary
import datetime
import os

while True:
    print("\n--- DAILY DIARY ---")
    print("1. Add today's entry")
    print("2. View all entries")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        entry = input("Write your diary entry: ")
        today = datetime.date.today()
        with open("diary.txt", "a") as file:
            file.write(str(today) + "\n")
            file.write(entry + "\n")
        print("Entry saved successfully!")
    elif choice == "2":
        if os.path.exists("diary.txt"):
            with open("diary.txt", "r") as file:
                print(file.read())
        else:
            print("No entries yet")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")

# Challenge: CSV result sheet

import csv
import json

students = [
    {"name": "Ali", "marks": [80, 90, 85]},
    {"name": "Sara", "marks": [95, 92, 98]},
    {"name": "Ahmed", "marks": [70, 75, 80]}
]

results = []

for student in students:
    marks = student["marks"]
    average = sum(marks) / 3

    results.append({
        "name": student["name"],
        "mark1": marks[0],
        "mark2": marks[1],
        "mark3": marks[2],
        "average": average
    })
with open("results.csv", "w", newline="") as file:
    fieldnames = ["name", "mark1", "mark2",
                  "mark3", "average"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(results)

print("CSV file saved!")
with open("results.json", "w") as file:
    json.dump(results, file, indent=4)

print("JSON file saved!")



import csv

with open("results.csv", "r") as file:

    reader = csv.DictReader(file)

    students = list(reader)

if students:
    topper = max(students, key=lambda x: float(x["average"]))

    print("Class Topper:", topper["name"])
    print("Average Marks:", topper["average"])

else:
    print("No student records found!")
