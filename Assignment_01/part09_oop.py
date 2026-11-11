"""
Name : Aimen Saeed
Trainee ID : TRN-2026-000352
Date : 10-11-26
"""
# Warm-up:
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks = []
    def add_mark(self, mark):
        self.marks.append(mark)
    def average(self):
        if len(self.marks) == 0:
            return 0
        return sum(self.marks) / len(self.marks)
    def __str__(self):
        return f"{self.name} (Roll {self.roll_no}): avg {self.average():.1f}"

s1 = Student("Ali", 12)
s1.add_mark(80)
s1.add_mark(85)
s1.add_mark(78)
print(s1)

# Build:
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.history = []
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance += amount
        self.history.append(f"Deposited Rs {amount}")
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
        self.history.append(f"Withdrawn Rs {amount}")
    def show_history(self):
        for transaction in self.history:
            print(transaction)
account = BankAccount("Ali", 1000)
account.deposit(500)
account.withdraw(200)
print("Balance:", account.balance)
account.show_history()

# Challenge:

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
    def __str__(self):
        return f"{self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size
    def __str__(self):
        return f"{self.title} by {self.author} ({self.file_size} MB)"

class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
    def borrow(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                print("Book borrowed!")
                return
        print("Book unavailable!")
    def return_book(self, title):
        for book in self.books:
            if book.title == title and not book.available:
                book.available = True
                print("Book returned!")
                return
        print("Book not found or already available!")
    def available_books(self):
        for book in self.books:
            if book.available:
                print(book)
library = Library()
library.add_book(Book("Python Basics", "Ali"))
library.add_book(EBook("AI Guide", "Sara", 5))
library.borrow("Python Basics")
print("\nAvailable books:")
library.available_books()
