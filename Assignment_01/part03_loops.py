"""
Name : Aimen Saeed
Trainee ID : TRN-2026-000352
Date : 10-11-26
"""

# Warm-up: Times Table
number = int(input("Enter a number to print its times table: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number*i}")

# Build: ATM PIN Check
correct_pin = 4321
tries = 0
while tries < 3:
    entered_pin = int(input("Enter your ATM PIN: "))
    if entered_pin == correct_pin:
        print("PIN accepted. Access granted.")
        break
    else:
        tries += 1
        print(f"Incorrect PIN. You have {3 - tries} attempts left.")

# Challenge: Numbwer Guessing Game
import random
secret_number = random.randint(1, 100)
guess=None
tries=0
while guess != secret_number:
    guess = int(input("Guess the secret number (between 1 and 100): "))
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the secret number.")
    tries += 1
print(f"You guessed the number in {tries} tries.")
