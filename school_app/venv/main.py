from school.grades import calculate_average, check_grade
from school.attendence import attendance_percentage

marks = [80, 90, 70]

average = calculate_average(marks)
grade = check_grade(average)

attendance = attendance_percentage(18, 20)

print("Average:", average)
print("Grade:", grade)
print("Attendance:", attendance, "%")