"""
Name : Aimen Saeed
Trainee ID : TRN-2026-000352
Date : 10-11-26
"""

# Warm-up:
marks = [90, 25, 70]
passing = []

for m in range(len(marks) - 1):
    if marks[m] > 33:
        passing = [marks[m]]

print(sum(passing) / len(marks))

