"""
Name : Aimen Saeed
Trainee ID : TRN-2026-000352
Date : 10-11-26
"""
# Warm-up:
import math
import random
import datetime
import statistics
print("Square root:", math.sqrt(144))
students = ["Ali", "Sara", "Ahmed", "Ayesha"]
print("Random student:", random.choice(students))
today = datetime.date.today()
end_date = datetime.date(today.year, 12, 31)
days_left = (end_date - today).days
print("Days left until 31 December:", days_left)
marks = [75, 80, 90, 65, 85]
print("Mean:", statistics.mean(marks))
print("Median:", statistics.median(marks))
